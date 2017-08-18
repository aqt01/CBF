from membership.models import Member
from sermons.models import Sermon
import datetime
from CBF.settings.local import TIME_ZONE

from sermons.models import Sermon
from events.models import Event
from thoughts.models import Thought


def elements_text_search(search_text):
    search_result_elements = list()
    search_result_elements.append( Sermon.objects.filter(name__contains=search_text))
    search_result_elements.append(Event.objects.filter(name__contains=search_text))
    search_result_elements.append(Thought.objects.filter(name__contains=search_text))
    elements = set()

    for search_set in search_result_elements:
        for element in search_set:
            elements.add(element)

    return elements

def elements_related_by_tags(tags, element):
    number_elements_related = 0
    elements_related = set()

    for tag in tags:
        number_elements_related += tag.get_count_related_objects()

    # If no topics related. we show last elements of this category
    if (number_elements_related < 4):
        return element.objects.all().order_by('date_created')[0:3]

    else:
        for tag in tags:
            if ( tag.thought_set.count() > 0 ):
                for thought in tag.thought_set.all():
                    elements_related.add(thought)
            if (tag.sermon_set.count() > 0):
                for sermon in tag.sermon_set.all():
                    elements_related.add(sermon)
            if (tag.event_set.count() > 0):
                for event in tag.event_set.all():
                    elements_related.add(event)
    return elements_related

def syncronize_with_youtube(title, video_id, description):
    elements = title.split(' | ')
    elements.append(description)
    elements.append('https://www.youtube.com/watch?=' + video_id)
    member = None

    try:
        sermon_exist = Sermon.objects.get(name=elements[0])
        return

    except Exception:
        print( " working with " + title)
        try:
            member = Member.objects.get(name=elements[1])
            date_created = datetime.datetime.strptime(elements[2], '%d/%m/%Y')
            date_created = date_created.replace(tzinfo=TIME_ZONE)
            sermon = Sermon.objects.create(name=elements[0], author=member,date_created=date_created,
            is_published=True,content=elements[3],url=elements[4])
            sermon.save()

        except Exception:
            print("Author Doesnt exist in database for sermon: " + title)
            return

        print("Failed to save " + title)
        print(Exception)
        return

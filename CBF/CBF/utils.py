from CBF.settings.local import TIME_ZONE
from CBF.settings.base import BASE_DIR

import boto3
import datetime
import os

from membership.models import Member
from sermons.models import Sermon, Tag
from events.models import Event
from thoughts.models import Thought


# Download the secrets json necessary for fetching data from youtube
def download_secrets():
    s3 = boto3.client('s3')
    bucket_secret_name = os.environ.get('AWS_STORAGE_BUCKET_SECRET_NAME')
    list = s3.list_objects(Bucket=bucket_secret_name)['Contents']
    for s3_key in list:
        s3_object = s3_key['Key']
        if not s3_object.endswith("/"):
            s3.download_file(bucket_secret_name, s3_object, BASE_DIR + '/' + s3_object)
        else:
            if not os.path.exists(s3_object):
                os.makedirs(s3_object)


# Search a text string in the different elements (sermon, event, thoughts)
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


# Searchs all elements related to this tag
# return a set of tags
def search_elements_related_by_tags(tag_name, max_elements):
    elements_related = set()
    tag = Tag.objects.filter(name=tag_name).first()

    if (tag.thought_set.count() > 0):
        for thought in tag.thought_set.all():
            elements_related.add(thought)
    if (tag.sermon_set.count() > 0):
        for sermon in tag.sermon_set.all():
            elements_related.add(sermon)
    if (tag.event_set.count() > 0):
        for event in tag.event_set.all():
            elements_related.add(event)
    return elements_related


# Searchs all elements of the same type related to various tags
def elements_related_by_tags(tags, element, element_object):
    number_elements_related = 0
    elements_related = set()

    for tag in tags:
        number_elements_related += tag.get_count_related_objects()

    # If no topics related. we show last elements of this category
    if (number_elements_related < 3):
        return element.objects.all().order_by('date_created')[0:2]

    else:
        for tag in tags:
            if (tag.thought_set.count() > 0):
                for thought in tag.thought_set.all():
                    if (len(elements_related) == 2):
                        break
                    elements_related.add(thought)
            if (tag.sermon_set.count() > 0):
                for sermon in tag.sermon_set.all():
                    if (len(elements_related) == 2):
                        break
                    elements_related.add(sermon)


    # Eliminate the same object in detail view
    elements_related.discard(element_object)
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
            is_published=True, content=elements[3],url=elements[4])
            sermon.save()

        except Exception:
            print("Author Doesnt exist in database for sermon: " + title)
            return

        print("Failed to save " + title)
        print(Exception)
        return

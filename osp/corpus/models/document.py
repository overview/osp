

from osp.common.models.base import BaseModel
from peewee import *


class Document(BaseModel):


    path = CharField(unique=True)
    stored_id = CharField(null=True)


    class Meta:
        db_name = 'document'

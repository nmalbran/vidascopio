# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Menu.titulo'
        db.add_column(u'web2_menu', 'titulo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=254),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Menu.titulo'
        db.delete_column(u'web2_menu', 'titulo')


    models = {
        u'web2.menu': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'web2.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'autor_cita': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cita': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menus': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web2.Menu']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'texto': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['web2']
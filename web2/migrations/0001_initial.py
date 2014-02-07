# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'web2_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('orden', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'web2', ['Menu'])

        # Adding model 'Pagina'
        db.create_table(u'web2_pagina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('cita', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('autor_cita', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'web2', ['Pagina'])

        # Adding M2M table for field menus on 'Pagina'
        m2m_table_name = db.shorten_name(u'web2_pagina_menus')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pagina', models.ForeignKey(orm[u'web2.pagina'], null=False)),
            ('menu', models.ForeignKey(orm[u'web2.menu'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pagina_id', 'menu_id'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table(u'web2_menu')

        # Deleting model 'Pagina'
        db.delete_table(u'web2_pagina')

        # Removing M2M table for field menus on 'Pagina'
        db.delete_table(db.shorten_name(u'web2_pagina_menus'))


    models = {
        u'web2.menu': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
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
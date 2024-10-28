2024-9/20～

プログラミングコンテスト

09月20日-開始

11月28日-中間発表

02月??日-本番

プロジェクト名 : procon_group_e (アンダーバー消えてます)

アプリケーション名 : reception_system (アンダーバー消えてます)

アプリケーション名 : base_app (アンダーバー消えてます) base置くファイル

python manage.py runserver

python manage.py makemigrations

python manage.py migrates

#htmlの最初に記載

ーーーーーーーーーーーーーーーーーーーーーーーーー

  {% extends 'base_app/base.html' %}
  {% load static %}
  
  {% block title%}
  {% endblock %}
  
  {% block contents %}
  {% endblock %}

ーーーーーーーーーーーーーーーーーーーーーーーーー

メモ

・各アプリのtemplatesの中に各アプリ名のフォルダを追加してください(そうでないとbaseを持ってこれなくなります)

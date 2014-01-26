#coding: utf-8
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ui.settings")
    from app.models import Photo
    Photo(url='http://img3.douban.com/mpic/s6586365.jpg').save()
    Photo(url='http://img5.douban.com/mpic/s4457709.jpg').save()
    Photo(url='http://img5.douban.com/mpic/s1915036.jpg').save()
    Photo(url='http://img5.douban.com/mpic/s10345469.jpg').save()
    Photo(url='http://img3.douban.com/mpic/s3340712.jpg').save()
    Photo(url='http://img3.douban.com/mpic/s1074361.jpg').save()
    Photo(url='http://img3.douban.com/mpic/s1517284.jpg').save()
    Photo(url='http://img3.douban.com/mpic/s2351323.jpg').save()

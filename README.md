<div align="center">
      <h1> <img src="https://github.com/ahammadmejbah/IBM-Project-02-Transform-Photos-to-Sketches-and-Paintings-with-OpenCV/blob/main/Additional%20Files/SN_web_lightmode.svg" width="300px"><br/>IBM Project 04 Build a Personal Movie Recommender with Django</h1>
     </div>

<p align="center"> <a href="https://github.com/ahammadmejbah" target="_blank"><img alt="" src="https://img.shields.io/badge/Website-EA4C89?style=normal&logo=dribbble&logoColor=white" style="vertical-align:center" /></a> <a href="https://twitter.com/ahammadmejbah" target="_blank"><img alt="" src="https://img.shields.io/badge/Twitter-1DA1F2?style=normal&logo=twitter&logoColor=white" style="vertical-align:center" /></a> <a href="https://www.facebook.com/ahammadmejbah" target="_blank"><img alt="" src="https://img.shields.io/badge/Facebook-1877F2?style=normal&logo=facebook&logoColor=white" style="vertical-align:center" /></a> <a href="https://www.instagram.com/ahammadmejbah/" target="_blank"><img alt="" src="https://img.shields.io/badge/Instagram-E4405F?style=normal&logo=instagram&logoColor=white" style="vertical-align:center" /></a> <a href="https://www.linkedin.com/in/ahammadmejbah/}" target="_blank"><img alt="" src="https://img.shields.io/badge/LinkedIn-0077B5?style=normal&logo=linkedin&logoColor=white" style="vertical-align:center" /></a> </p>

### Admin Panel: 

``` python
from django.contrib import admin

# Register your models here.

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    fields = ['imdb_id', 'genres', 'original_title', 'overview', 'watched']
    list_display = ('original_title', 'genres', 'release_date', 'watched')
    search_fields = ['original_title', 'overview']


admin.site.register(Movie, MovieAdmin)


```

### Recommender Models 
``` python
from django.db import models


# Create your models here.
# HINT: Create a Movie model here
# It will be mapped to a database table with columns
class Movie(models.Model):
    """
    Django Movie Model
    """
    # IMDB id
    imdb_id = models.CharField(max_length=48, null=False)
    # Movie genres
    genres = models.CharField(max_length=200, null=True)
    # Original language
    original_language = models.CharField(max_length=20, null=True)
    # Original movie title
    original_title = models.CharField(max_length=500, null=False)
    # Movie release date
    release_date = models.IntegerField(default=1970)
    # Movie overview
    overview = models.TextField(max_length=2000, null=True)
    # Average voting for the movie
    vote_average = models.FloatField(default=0)
    # Total votes for ths movie
    vote_count = models.IntegerField(default=0)
    # The movie's poster path
    poster_path = models.CharField(max_length=64, null=True)
    # If you have watched this movie
    watched = models.BooleanField(default=False, null=True)
    # If this movie will be recommended
    recommended = models.BooleanField(default=False, null=True)

```

![image](https://github.com/ahammadmejbah/IBM-Project-04-Build-a-Personal-Movie-Recommender-with-Django/assets/56669333/dc602426-e1ab-4e8b-9110-586f019340c3)
![image](https://github.com/ahammadmejbah/IBM-Project-04-Build-a-Personal-Movie-Recommender-with-Django/assets/56669333/4bab4e34-f62a-4111-9769-93f8aa53d509)
![image](https://github.com/ahammadmejbah/IBM-Project-04-Build-a-Personal-Movie-Recommender-with-Django/assets/56669333/1f5fc43b-9532-46af-a710-9b00f8809a01)
![image](https://github.com/ahammadmejbah/IBM-Project-04-Build-a-Personal-Movie-Recommender-with-Django/assets/56669333/0f319a58-73d4-4935-b92b-48022e32d6be)
![image](https://github.com/ahammadmejbah/IBM-Project-04-Build-a-Personal-Movie-Recommender-with-Django/assets/56669333/1c545f35-d9d4-4c73-9fa8-50bf03caaa44)


### Review a Predefined Movie Model
In this template app, we have created a Movie model for you. To review this model, simply go to
recommender/movierecommender/models.py and find the Movie class.

This Movie class extends from Django models.Model super class.
The Django models provides a set of Object-Relationship Mapping APIs such as mapping your sub-class
into a database table, insert/update/delete database records, mapping database records into objects, etc.

The defined Movie class contains the following fields:

* imdb_id: IMDB id
* genres: Movie genres like animation, family, action science fiction, etc.
* original_language: Movie original language
* original_title: Movie title
* release_date: Movie release date, year only
* overview: The overview or short description of the movie
* vote_average: Average voting for the movie
* vote_count: Total vote counts for the movie, may reflect the popularity
* poster_path: The relative URL of movie poster image
* watched: If you have watched the movie
* recommended: If the movie has been recommended to you

After the Django migration you executed earlier, Django Model will also create a movie table automatically in our SQLite database with
corresponding columns.




Author(s)
<a href="https://www.linkedin.com/in/yan-luo-96288783/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkGuidedProjectsbuildapersonalmovierecommenderwithdjango450-2023-01-01">Yan Luo</a>

Other Contributor(s)
Changelog
Date	Version	Changed by	Change Description
2021-08-10	0.1	Yan Luo	Initial version created
© IBM Corporation 2023. All rights reserved.
<!-- </> with 💛 by readMD (https://readmd.itsvg.in) -->
    

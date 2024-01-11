My approach regarding developing this website: DJ-Naresh

1.Project setup: starting from first i have created django project Favourite Tune were ihave create django app Tune tracker by this i have register the app in settings,created super user, installed virtual environment
2.Model Creation: Created 2 models inside Tunetracker app with artist having one field linked by foreign key with songs model artistname ,also if any artist is deleted the whole songs relevent to him will be deledte using CASCADE on delete.Soongs model have 4 colomns with sorng url and image url i have added extra with the artist and song name.then did make migrations, migrate.
3. Adding Songs: For adding songs i have think about to embed the soundcloud songs url link as it would have better visual display with sound deployed on cloud just need url so i picked from there and added on datebade with name,artist name by searching on google and the thumbnail of song has been taken from any online image url
4.Creating the Template and static files: So for this i have created template folder inside that all my html files are there and all images css javasacript files are present inside static inside assets directory.
5.Home page:inside the home page i have try to display about website and then below that i have dosplayed only 8 songs from database just to represent so i have collected the songs from database and displyed by using django-html it contains navbar ,footer header and embedeed in ifraame the songs from sound cloud wihich consist of playbutton.
6.Albums Page: this page is design to diplay all songs present in database in blog list manner and contain artist detail also so here also we can play songs as it was emebeded via iframe using django html for loop it was diplayed all songs.
7.Artist Page: so here we pick all artist from database and display it via django html for loop like in blog card with clickable artist name link now on clicking the link we get redirected to new page artistsongs.
8. Artist song page: this was a bit crucial part were i have passes the artist name on the url via href tag of html to send artistname and then in views.py i try to check wheter this artist present in database then find its name from django iexact query and then using name of artist we pull all songs from databse by comparing artist name and sended the data in paarams to display on artist song url list all songs with artist name and also song count is also there
9. Upload songs Page: So here is the last stuff were form is created and it validate using javascript function i used Post method and using action i pass vvalid data to views function on django and pulled all data of form then we first try to find artist name we get on data base if it is already existed then just add the songs with the artist name given on data base else if artist not exist earlier then we first add that artist on data base then add wholle tuple of song data on database and redirected to home page and data will stored on database.
10.How to run? For this i have added readme in github and also requiremnt .txt file so first install requirement .txt file and then no need to create virtual env just run python manage.py runserver goto the link it will gonna display
and to look admin panel 
Username: admin
password: 12345






















 

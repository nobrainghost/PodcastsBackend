# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApplePodcastsAustraliaAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_all_podcasts'


class ApplePodcastsAustraliaAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_all_podcasts_—_episodes'


class ApplePodcastsAustraliaArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_arts'


class ApplePodcastsAustraliaArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_arts_—_episodes'


class ApplePodcastsAustraliaBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_business'


class ApplePodcastsAustraliaBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_business_—_episodes'


class ApplePodcastsAustraliaComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_comedy'


class ApplePodcastsAustraliaComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_comedy_—_episodes'


class ApplePodcastsAustraliaEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_education'


class ApplePodcastsAustraliaEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_education_—_episodes'


class ApplePodcastsAustraliaFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_fiction'


class ApplePodcastsAustraliaFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_fiction_—_episodes'


class ApplePodcastsAustraliaGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_government'


class ApplePodcastsAustraliaGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_government_—_episodes'


class ApplePodcastsAustraliaHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_history'


class ApplePodcastsAustraliaHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_history_—_episodes'


class ApplePodcastsAustraliaLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_leisure'


class ApplePodcastsAustraliaLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_leisure_—_episodes'


class ApplePodcastsAustraliaMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_music'


class ApplePodcastsAustraliaMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_music_—_episodes'


class ApplePodcastsAustraliaNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_news'


class ApplePodcastsAustraliaNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_news_—_episodes'


class ApplePodcastsAustraliaScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_science'


class ApplePodcastsAustraliaScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_science_—_episodes'


class ApplePodcastsAustraliaSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_sports'


class ApplePodcastsAustraliaSportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_sports_—_episodes'


class ApplePodcastsAustraliaTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_technology'


class ApplePodcastsAustraliaTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_technology_—_episodes'


class ApplePodcastsAustraliaTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_true_crime'


class ApplePodcastsAustraliaTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_australia_—_true_crime_—_episodes'


class ApplePodcastsCanadaAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_all_podcasts'


class ApplePodcastsCanadaAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_all_podcasts_—_episodes'


class ApplePodcastsCanadaArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_arts'


class ApplePodcastsCanadaArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_arts_—_episodes'


class ApplePodcastsCanadaBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_business'


class ApplePodcastsCanadaBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_business_—_episodes'


class ApplePodcastsCanadaComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_comedy'


class ApplePodcastsCanadaComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_comedy_—_episodes'


class ApplePodcastsCanadaEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_education'


class ApplePodcastsCanadaEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_education_—_episodes'


class ApplePodcastsCanadaFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_fiction'


class ApplePodcastsCanadaFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_fiction_—_episodes'


class ApplePodcastsCanadaGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_government'


class ApplePodcastsCanadaGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_government_—_episodes'


class ApplePodcastsCanadaHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_history'


class ApplePodcastsCanadaHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_history_—_episodes'


class ApplePodcastsCanadaLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_leisure'


class ApplePodcastsCanadaLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_leisure_—_episodes'


class ApplePodcastsCanadaMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_music'


class ApplePodcastsCanadaMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_music_—_episodes'


class ApplePodcastsCanadaNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_news'


class ApplePodcastsCanadaNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_news_—_episodes'


class ApplePodcastsCanadaScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_science'


class ApplePodcastsCanadaScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_science_—_episodes'


class ApplePodcastsCanadaSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_sports'


class ApplePodcastsCanadaSportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_sports_—_episodes'


class ApplePodcastsCanadaTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_technology'


class ApplePodcastsCanadaTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_technology_—_episodes'


class ApplePodcastsCanadaTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_true_crime'


class ApplePodcastsCanadaTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_canada_—_true_crime_—_episodes'


class ApplePodcastsFranceAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_all_podcasts'


class ApplePodcastsFranceAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_all_podcasts_—_episodes'


class ApplePodcastsFranceArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_arts'


class ApplePodcastsFranceArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_arts_—_episodes'


class ApplePodcastsFranceBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_business'


class ApplePodcastsFranceBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_business_—_episodes'


class ApplePodcastsFranceComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_comedy'


class ApplePodcastsFranceComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_comedy_—_episodes'


class ApplePodcastsFranceEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_education'


class ApplePodcastsFranceEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_education_—_episodes'


class ApplePodcastsFranceFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_fiction'


class ApplePodcastsFranceFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_fiction_—_episodes'


class ApplePodcastsFranceGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_government'


class ApplePodcastsFranceGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_government_—_episodes'


class ApplePodcastsFranceHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_history'


class ApplePodcastsFranceHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_history_—_episodes'


class ApplePodcastsFranceLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_leisure'


class ApplePodcastsFranceLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_leisure_—_episodes'


class ApplePodcastsFranceMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_music'


class ApplePodcastsFranceMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_music_—_episodes'


class ApplePodcastsFranceNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_news'


class ApplePodcastsFranceNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_news_—_episodes'


class ApplePodcastsFranceScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_science'


class ApplePodcastsFranceScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_science_—_episodes'


class ApplePodcastsFranceSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_sports'


class ApplePodcastsFranceSportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_sports_—_episodes'


class ApplePodcastsFranceTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_technology'


class ApplePodcastsFranceTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_technology_—_episodes'


class ApplePodcastsFranceTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_true_crime'


class ApplePodcastsFranceTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_france_—_true_crime_—_episodes'


class ApplePodcastsGermanyAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_all_podcasts'


class ApplePodcastsGermanyAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_all_podcasts_—_episodes'


class ApplePodcastsGermanyArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_arts'


class ApplePodcastsGermanyArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_arts_—_episodes'


class ApplePodcastsGermanyBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_business'


class ApplePodcastsGermanyBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_business_—_episodes'


class ApplePodcastsGermanyComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_comedy'


class ApplePodcastsGermanyComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_comedy_—_episodes'


class ApplePodcastsGermanyEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_education'


class ApplePodcastsGermanyEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_education_—_episodes'


class ApplePodcastsGermanyFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_fiction'


class ApplePodcastsGermanyFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_fiction_—_episodes'


class ApplePodcastsGermanyGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_government'


class ApplePodcastsGermanyGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_government_—_episodes'


class ApplePodcastsGermanyHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_history'


class ApplePodcastsGermanyHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_history_—_episodes'


class ApplePodcastsGermanyLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_leisure'


class ApplePodcastsGermanyLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_leisure_—_episodes'


class ApplePodcastsGermanyMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_music'


class ApplePodcastsGermanyMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_music_—_episodes'


class ApplePodcastsGermanyNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_news'


class ApplePodcastsGermanyNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_news_—_episodes'


class ApplePodcastsGermanyScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_science'


class ApplePodcastsGermanyScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_science_—_episodes'


class ApplePodcastsGermanySports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_sports'


class ApplePodcastsGermanySportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_sports_—_episodes'


class ApplePodcastsGermanyTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_technology'


class ApplePodcastsGermanyTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_technology_—_episodes'


class ApplePodcastsGermanyTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_true_crime'


class ApplePodcastsGermanyTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_germany_—_true_crime_—_episodes'


class ApplePodcastsGreatBritainAfterShows(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_after_shows'


class ApplePodcastsGreatBritainAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_all_podcasts'


class ApplePodcastsGreatBritainAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_all_podcasts_—_episodes'


class ApplePodcastsGreatBritainAlternativeHealth(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_alternative_health'


class ApplePodcastsGreatBritainAlternativeHealthEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_alternative_health_—_episodes'


class ApplePodcastsGreatBritainArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_arts'


class ApplePodcastsGreatBritainArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_arts_—_episodes'


class ApplePodcastsGreatBritainAstronomy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_astronomy'


class ApplePodcastsGreatBritainAstronomyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_astronomy_—_episodes'


class ApplePodcastsGreatBritainAutomotive(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_automotive'


class ApplePodcastsGreatBritainAutomotiveEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_automotive_—_episodes'


class ApplePodcastsGreatBritainAviation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_aviation'


class ApplePodcastsGreatBritainAviationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_aviation_—_episodes'


class ApplePodcastsGreatBritainBaseball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_baseball'


class ApplePodcastsGreatBritainBaseballEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_baseball_—_episodes'


class ApplePodcastsGreatBritainBasketball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_basketball'


class ApplePodcastsGreatBritainBasketballEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_basketball_—_episodes'


class ApplePodcastsGreatBritainBooks(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_books'


class ApplePodcastsGreatBritainBooksEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_books_—_episodes'


class ApplePodcastsGreatBritainBuddhism(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_buddhism'


class ApplePodcastsGreatBritainBuddhismEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_buddhism_—_episodes'


class ApplePodcastsGreatBritainBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_business'


class ApplePodcastsGreatBritainBusinessNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_business_news'


class ApplePodcastsGreatBritainBusinessNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_business_news_—_episodes'


class ApplePodcastsGreatBritainBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_business_—_episodes'


class ApplePodcastsGreatBritainCareers(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_careers'


class ApplePodcastsGreatBritainCareersEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_careers_—_episodes'


class ApplePodcastsGreatBritainChemistry(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_chemistry'


class ApplePodcastsGreatBritainChemistryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_chemistry_—_episodes'


class ApplePodcastsGreatBritainChristianity(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_christianity'


class ApplePodcastsGreatBritainChristianityEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_christianity_—_episodes'


class ApplePodcastsGreatBritainComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_comedy'


class ApplePodcastsGreatBritainComedyFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_comedy_fiction'


class ApplePodcastsGreatBritainComedyFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_comedy_fiction_—_episodes'


class ApplePodcastsGreatBritainComedyInterviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_comedy_interviews'


class ApplePodcastsGreatBritainComedyInterviewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_comedy_interviews_—_episodes'


class ApplePodcastsGreatBritainComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_comedy_—_episodes'


class ApplePodcastsGreatBritainCourses(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_courses'


class ApplePodcastsGreatBritainCoursesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_courses_—_episodes'


class ApplePodcastsGreatBritainCrafts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_crafts'


class ApplePodcastsGreatBritainCraftsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_crafts_—_episodes'


class ApplePodcastsGreatBritainCricket(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_cricket'


class ApplePodcastsGreatBritainDailyNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_daily_news'


class ApplePodcastsGreatBritainDailyNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_daily_news_—_episodes'


class ApplePodcastsGreatBritainDesign(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_design'


class ApplePodcastsGreatBritainDesignEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_design_—_episodes'


class ApplePodcastsGreatBritainDocumentary(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_documentary'


class ApplePodcastsGreatBritainDocumentaryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_documentary_—_episodes'


class ApplePodcastsGreatBritainDrama(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_drama'


class ApplePodcastsGreatBritainDramaEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_drama_—_episodes'


class ApplePodcastsGreatBritainEarthSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_earth_sciences'


class ApplePodcastsGreatBritainEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_education'


class ApplePodcastsGreatBritainEducationForKids(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_education_for_kids'


class ApplePodcastsGreatBritainEducationForKidsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_education_for_kids_—_episodes'


class ApplePodcastsGreatBritainEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_education_—_episodes'


class ApplePodcastsGreatBritainEntertainmentNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_entertainment_news'


class ApplePodcastsGreatBritainEntertainmentNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_entertainment_news_—_episodes'


class ApplePodcastsGreatBritainEntrepreneurship(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_entrepreneurship'


class ApplePodcastsGreatBritainEntrepreneurshipEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_entrepreneurship_—_episodes'


class ApplePodcastsGreatBritainFantasySports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_fantasy_sports'


class ApplePodcastsGreatBritainFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_fiction'


class ApplePodcastsGreatBritainFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_fiction_—_episodes'


class ApplePodcastsGreatBritainFilmHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_film_history'


class ApplePodcastsGreatBritainFilmInterviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_film_interviews'


class ApplePodcastsGreatBritainFilmReviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_film_reviews'


class ApplePodcastsGreatBritainFitness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_fitness'


class ApplePodcastsGreatBritainFitnessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_fitness_—_episodes'


class ApplePodcastsGreatBritainFood(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_food'


class ApplePodcastsGreatBritainFoodEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_food_—_episodes'


class ApplePodcastsGreatBritainFootball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_football'


class ApplePodcastsGreatBritainGames(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_games'


class ApplePodcastsGreatBritainGolf(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_golf'


class ApplePodcastsGreatBritainGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_government'


class ApplePodcastsGreatBritainGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_government_—_episodes'


class ApplePodcastsGreatBritainHinduism(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_hinduism'


class ApplePodcastsGreatBritainHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_history'


class ApplePodcastsGreatBritainHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_history_—_episodes'


class ApplePodcastsGreatBritainHobbies(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_hobbies'


class ApplePodcastsGreatBritainHobbiesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_hobbies_—_episodes'


class ApplePodcastsGreatBritainHockey(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_hockey'


class ApplePodcastsGreatBritainHowTo(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_how_to'


class ApplePodcastsGreatBritainHowToEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_how_to_—_episodes'


class ApplePodcastsGreatBritainImprov(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_improv'


class ApplePodcastsGreatBritainImprovEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_improv_—_episodes'


class ApplePodcastsGreatBritainInvesting(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_investing'


class ApplePodcastsGreatBritainInvestingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_investing_—_episodes'


class ApplePodcastsGreatBritainIslam(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_islam'


class ApplePodcastsGreatBritainIslamEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_islam_—_episodes'


class ApplePodcastsGreatBritainJudaism(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_judaism'


class ApplePodcastsGreatBritainJudaismEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_judaism_—_episodes'


class ApplePodcastsGreatBritainLanguageLearning(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_language_learning'


class ApplePodcastsGreatBritainLanguageLearningEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_language_learning_—_episodes'


class ApplePodcastsGreatBritainLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_leisure'


class ApplePodcastsGreatBritainLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_leisure_—_episodes'


class ApplePodcastsGreatBritainLifeSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_life_sciences'


class ApplePodcastsGreatBritainLifeSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_life_sciences_—_episodes'


class ApplePodcastsGreatBritainManagement(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_management'


class ApplePodcastsGreatBritainManagementEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_management_—_episodes'


class ApplePodcastsGreatBritainMarketing(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_marketing'


class ApplePodcastsGreatBritainMarketingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_marketing_—_episodes'


class ApplePodcastsGreatBritainMathematics(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_mathematics'


class ApplePodcastsGreatBritainMathematicsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_mathematics_—_episodes'


class ApplePodcastsGreatBritainMedicine(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_medicine'


class ApplePodcastsGreatBritainMedicineEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_medicine_—_episodes'


class ApplePodcastsGreatBritainMentalHealth(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_mental_health'


class ApplePodcastsGreatBritainMentalHealthEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_mental_health_—_episodes'


class ApplePodcastsGreatBritainMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music'


class ApplePodcastsGreatBritainMusicCommentary(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_commentary'


class ApplePodcastsGreatBritainMusicCommentaryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_commentary_—_episodes'


class ApplePodcastsGreatBritainMusicHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_history'


class ApplePodcastsGreatBritainMusicHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_history_—_episodes'


class ApplePodcastsGreatBritainMusicInterviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_interviews'


class ApplePodcastsGreatBritainMusicInterviewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_interviews_—_episodes'


class ApplePodcastsGreatBritainMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_music_—_episodes'


class ApplePodcastsGreatBritainNaturalSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_natural_sciences'


class ApplePodcastsGreatBritainNaturalSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_natural_sciences_—_episodes'


class ApplePodcastsGreatBritainNature(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_nature'


class ApplePodcastsGreatBritainNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_news'


class ApplePodcastsGreatBritainNewsCommentary(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_news_commentary'


class ApplePodcastsGreatBritainNewsCommentaryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_news_commentary_—_episodes'


class ApplePodcastsGreatBritainNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_news_—_episodes'


class ApplePodcastsGreatBritainNonProfit(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_non_profit'


class ApplePodcastsGreatBritainNonProfitEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_non_profit_—_episodes'


class ApplePodcastsGreatBritainNutrition(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_nutrition'


class ApplePodcastsGreatBritainNutritionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_nutrition_—_episodes'


class ApplePodcastsGreatBritainParenting(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_parenting'


class ApplePodcastsGreatBritainParentingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_parenting_—_episodes'


class ApplePodcastsGreatBritainPerformingArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_performing_arts'


class ApplePodcastsGreatBritainPerformingArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_performing_arts_—_episodes'


class ApplePodcastsGreatBritainPersonalJournals(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_personal_journals'


class ApplePodcastsGreatBritainPersonalJournalsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_personal_journals_—_episodes'


class ApplePodcastsGreatBritainPhilosophy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_philosophy'


class ApplePodcastsGreatBritainPhysics(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_physics'


class ApplePodcastsGreatBritainPhysicsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_physics_—_episodes'


class ApplePodcastsGreatBritainPolitics(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_politics'


class ApplePodcastsGreatBritainPoliticsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_politics_—_episodes'


class ApplePodcastsGreatBritainRelationships(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_relationships'


class ApplePodcastsGreatBritainRelationshipsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_relationships_—_episodes'


class ApplePodcastsGreatBritainReligion(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_religion'


class ApplePodcastsGreatBritainReligionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_religion_—_episodes'


class ApplePodcastsGreatBritainRugby(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_rugby'


class ApplePodcastsGreatBritainRunning(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_running'


class ApplePodcastsGreatBritainScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_science'


class ApplePodcastsGreatBritainScienceFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_science_fiction'


class ApplePodcastsGreatBritainScienceFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_science_fiction_—_episodes'


class ApplePodcastsGreatBritainScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_science_—_episodes'


class ApplePodcastsGreatBritainSelfImprovement(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_self_improvement'


class ApplePodcastsGreatBritainSelfImprovementEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_self_improvement_—_episodes'


class ApplePodcastsGreatBritainSexuality(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_sexuality'


class ApplePodcastsGreatBritainSexualityEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_sexuality_—_episodes'


class ApplePodcastsGreatBritainSoccer(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_soccer'


class ApplePodcastsGreatBritainSocialSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_social_sciences'


class ApplePodcastsGreatBritainSocialSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_social_sciences_—_episodes'


class ApplePodcastsGreatBritainSpirituality(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_spirituality'


class ApplePodcastsGreatBritainSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_sports'


class ApplePodcastsGreatBritainSportsNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_sports_news'


class ApplePodcastsGreatBritainSportsNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_sports_news_—_episodes'


class ApplePodcastsGreatBritainSportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_sports_—_episodes'


class ApplePodcastsGreatBritainStandUp(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_stand_up'


class ApplePodcastsGreatBritainStandUpEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_stand_up_—_episodes'


class ApplePodcastsGreatBritainStoriesForKids(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_stories_for_kids'


class ApplePodcastsGreatBritainStoriesForKidsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_stories_for_kids_—_episodes'


class ApplePodcastsGreatBritainSwimming(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_swimming'


class ApplePodcastsGreatBritainTechNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_tech_news'


class ApplePodcastsGreatBritainTechNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_tech_news_—_episodes'


class ApplePodcastsGreatBritainTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_technology'


class ApplePodcastsGreatBritainTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_technology_—_episodes'


class ApplePodcastsGreatBritainTennis(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_tennis'


class ApplePodcastsGreatBritainTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_true_crime'


class ApplePodcastsGreatBritainTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_true_crime_—_episodes'


class ApplePodcastsGreatBritainTvReviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_tv_reviews'


class ApplePodcastsGreatBritainVideoGames(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_video_games'


class ApplePodcastsGreatBritainVideoGamesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_video_games_—_episodes'


class ApplePodcastsGreatBritainVisualArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_visual_arts'


class ApplePodcastsGreatBritainVisualArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_visual_arts_—_episodes'


class ApplePodcastsGreatBritainVolleyball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_volleyball'


class ApplePodcastsGreatBritainWilderness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_wilderness'


class ApplePodcastsGreatBritainWrestling(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_great_britain_—_wrestling'


class ApplePodcastsItalyAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_all_podcasts'


class ApplePodcastsItalyAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_all_podcasts_—_episodes'


class ApplePodcastsItalyArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_arts'


class ApplePodcastsItalyArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_arts_—_episodes'


class ApplePodcastsItalyBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_business'


class ApplePodcastsItalyBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_business_—_episodes'


class ApplePodcastsItalyComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_comedy'


class ApplePodcastsItalyComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_comedy_—_episodes'


class ApplePodcastsItalyEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_education'


class ApplePodcastsItalyEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_education_—_episodes'


class ApplePodcastsItalyFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_fiction'


class ApplePodcastsItalyFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_fiction_—_episodes'


class ApplePodcastsItalyGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_government'


class ApplePodcastsItalyGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_government_—_episodes'


class ApplePodcastsItalyHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_history'


class ApplePodcastsItalyHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_history_—_episodes'


class ApplePodcastsItalyLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_leisure'


class ApplePodcastsItalyLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_leisure_—_episodes'


class ApplePodcastsItalyMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_music'


class ApplePodcastsItalyMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_music_—_episodes'


class ApplePodcastsItalyNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_news'


class ApplePodcastsItalyNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_news_—_episodes'


class ApplePodcastsItalyScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_science'


class ApplePodcastsItalyScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_science_—_episodes'


class ApplePodcastsItalySports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_sports'


class ApplePodcastsItalySportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_sports_—_episodes'


class ApplePodcastsItalyTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_technology'


class ApplePodcastsItalyTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_technology_—_episodes'


class ApplePodcastsItalyTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_true_crime'


class ApplePodcastsItalyTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_italy_—_true_crime_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaAfterShows(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_after_shows'


class ApplePodcastsUnitedStatesOfAmericaAfterShowsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_after_shows_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaAllPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_all_podcasts'


class ApplePodcastsUnitedStatesOfAmericaAllPodcastsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_all_podcasts_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaAlternativeHealth(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_alternative_health'


class ApplePodcastsUnitedStatesOfAmericaAlternativeHealthEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_alternative_health_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_arts'


class ApplePodcastsUnitedStatesOfAmericaArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_arts_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaAstronomy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_astronomy'


class ApplePodcastsUnitedStatesOfAmericaAstronomyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_astronomy_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaAutomotive(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_automotive'


class ApplePodcastsUnitedStatesOfAmericaAutomotiveEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_automotive_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaAviation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_aviation'


class ApplePodcastsUnitedStatesOfAmericaAviationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_aviation_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaBaseball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_baseball'


class ApplePodcastsUnitedStatesOfAmericaBaseballEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_baseball_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaBasketball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_basketball'


class ApplePodcastsUnitedStatesOfAmericaBasketballEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_basketball_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaBooks(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_books'


class ApplePodcastsUnitedStatesOfAmericaBooksEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_books_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaBuddhism(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_buddhism'


class ApplePodcastsUnitedStatesOfAmericaBuddhismEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_buddhism_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_business'


class ApplePodcastsUnitedStatesOfAmericaBusinessNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_business_news'


class ApplePodcastsUnitedStatesOfAmericaBusinessNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_business_news_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaBusinessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_business_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaCareers(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_careers'


class ApplePodcastsUnitedStatesOfAmericaCareersEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_careers_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaChemistry(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_chemistry'


class ApplePodcastsUnitedStatesOfAmericaChemistryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_chemistry_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaChristianity(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_christianity'


class ApplePodcastsUnitedStatesOfAmericaChristianityEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_christianity_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_comedy'


class ApplePodcastsUnitedStatesOfAmericaComedyFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_comedy_fiction'


class ApplePodcastsUnitedStatesOfAmericaComedyFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_comedy_fiction_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaComedyInterviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_comedy_interviews'


class ApplePodcastsUnitedStatesOfAmericaComedyInterviewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_comedy_interviews_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaComedyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_comedy_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaCourses(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_courses'


class ApplePodcastsUnitedStatesOfAmericaCoursesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_courses_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaCrafts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_crafts'


class ApplePodcastsUnitedStatesOfAmericaCraftsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_crafts_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaCricket(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_cricket'


class ApplePodcastsUnitedStatesOfAmericaCricketEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_cricket_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaDailyNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_daily_news'


class ApplePodcastsUnitedStatesOfAmericaDailyNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_daily_news_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaDesign(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_design'


class ApplePodcastsUnitedStatesOfAmericaDesignEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_design_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaDocumentary(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_documentary'


class ApplePodcastsUnitedStatesOfAmericaDocumentaryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_documentary_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaDrama(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_drama'


class ApplePodcastsUnitedStatesOfAmericaDramaEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_drama_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaEarthSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_earth_sciences'


class ApplePodcastsUnitedStatesOfAmericaEarthSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_earth_sciences_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_education'


class ApplePodcastsUnitedStatesOfAmericaEducationForKids(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_education_for_kids'


class ApplePodcastsUnitedStatesOfAmericaEducationForKidsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_education_for_kids_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaEducationEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_education_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaEntertainmentNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_entertainment_news'


class ApplePodcastsUnitedStatesOfAmericaEntertainmentNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_entertainment_news_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaEntrepreneurship(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_entrepreneurship'


class ApplePodcastsUnitedStatesOfAmericaEntrepreneurshipEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_entrepreneurship_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFantasySports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_fantasy_sports'


class ApplePodcastsUnitedStatesOfAmericaFantasySportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_fantasy_sports_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_fiction'


class ApplePodcastsUnitedStatesOfAmericaFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_fiction_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFilmHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_film_history'


class ApplePodcastsUnitedStatesOfAmericaFilmHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_film_history_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFilmInterviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_film_interviews'


class ApplePodcastsUnitedStatesOfAmericaFilmInterviewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_film_interviews_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFilmReviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_film_reviews'


class ApplePodcastsUnitedStatesOfAmericaFitness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_fitness'


class ApplePodcastsUnitedStatesOfAmericaFitnessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_fitness_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFood(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_food'


class ApplePodcastsUnitedStatesOfAmericaFoodEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_food_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaFootball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_football'


class ApplePodcastsUnitedStatesOfAmericaFootballEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_football_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaGames(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_games'


class ApplePodcastsUnitedStatesOfAmericaGamesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_games_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaGolf(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_golf'


class ApplePodcastsUnitedStatesOfAmericaGolfEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_golf_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaGovernment(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_government'


class ApplePodcastsUnitedStatesOfAmericaGovernmentEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_government_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaHinduism(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_hinduism'


class ApplePodcastsUnitedStatesOfAmericaHinduismEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_hinduism_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_history'


class ApplePodcastsUnitedStatesOfAmericaHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_history_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaHobbies(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_hobbies'


class ApplePodcastsUnitedStatesOfAmericaHobbiesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_hobbies_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaHockey(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_hockey'


class ApplePodcastsUnitedStatesOfAmericaHockeyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_hockey_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaHowTo(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_how_to'


class ApplePodcastsUnitedStatesOfAmericaHowToEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_how_to_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaImprov(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_improv'


class ApplePodcastsUnitedStatesOfAmericaImprovEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_improv_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaInvesting(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_investing'


class ApplePodcastsUnitedStatesOfAmericaInvestingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_investing_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaIslam(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_islam'


class ApplePodcastsUnitedStatesOfAmericaIslamEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_islam_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaJudaism(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_judaism'


class ApplePodcastsUnitedStatesOfAmericaJudaismEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_judaism_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaLanguageLearning(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_language_learning'


class ApplePodcastsUnitedStatesOfAmericaLanguageLearningEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_language_learning_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_leisure'


class ApplePodcastsUnitedStatesOfAmericaLeisureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_leisure_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaLifeSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_life_sciences'


class ApplePodcastsUnitedStatesOfAmericaLifeSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_life_sciences_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaManagement(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_management'


class ApplePodcastsUnitedStatesOfAmericaManagementEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_management_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMarketing(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_marketing'


class ApplePodcastsUnitedStatesOfAmericaMarketingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_marketing_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMathematics(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_mathematics'


class ApplePodcastsUnitedStatesOfAmericaMathematicsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_mathematics_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMedicine(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_medicine'


class ApplePodcastsUnitedStatesOfAmericaMedicineEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_medicine_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMentalHealth(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_mental_health'


class ApplePodcastsUnitedStatesOfAmericaMentalHealthEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_mental_health_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music'


class ApplePodcastsUnitedStatesOfAmericaMusicCommentary(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_commentary'


class ApplePodcastsUnitedStatesOfAmericaMusicCommentaryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_commentary_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMusicHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_history'


class ApplePodcastsUnitedStatesOfAmericaMusicHistoryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_history_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMusicInterviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_interviews'


class ApplePodcastsUnitedStatesOfAmericaMusicInterviewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_interviews_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaMusicEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_music_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaNaturalSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_natural_sciences'


class ApplePodcastsUnitedStatesOfAmericaNaturalSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_natural_sciences_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaNature(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_nature'


class ApplePodcastsUnitedStatesOfAmericaNatureEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_nature_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_news'


class ApplePodcastsUnitedStatesOfAmericaNewsCommentary(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_news_commentary'


class ApplePodcastsUnitedStatesOfAmericaNewsCommentaryEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_news_commentary_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_news_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaNonProfit(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_non_profit'


class ApplePodcastsUnitedStatesOfAmericaNonProfitEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_non_profit_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaNutrition(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_nutrition'


class ApplePodcastsUnitedStatesOfAmericaNutritionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_nutrition_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaParenting(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_parenting'


class ApplePodcastsUnitedStatesOfAmericaParentingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_parenting_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaPerformingArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_performing_arts'


class ApplePodcastsUnitedStatesOfAmericaPerformingArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_performing_arts_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaPersonalJournals(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_personal_journals'


class ApplePodcastsUnitedStatesOfAmericaPersonalJournalsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_personal_journals_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaPhilosophy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_philosophy'


class ApplePodcastsUnitedStatesOfAmericaPhilosophyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_philosophy_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaPhysics(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_physics'


class ApplePodcastsUnitedStatesOfAmericaPhysicsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_physics_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaPolitics(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_politics'


class ApplePodcastsUnitedStatesOfAmericaPoliticsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_politics_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaRelationships(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_relationships'


class ApplePodcastsUnitedStatesOfAmericaRelationshipsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_relationships_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaReligion(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_religion'


class ApplePodcastsUnitedStatesOfAmericaReligionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_religion_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaRugby(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_rugby'


class ApplePodcastsUnitedStatesOfAmericaRugbyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_rugby_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaRunning(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_running'


class ApplePodcastsUnitedStatesOfAmericaRunningEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_running_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_science'


class ApplePodcastsUnitedStatesOfAmericaScienceFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_science_fiction'


class ApplePodcastsUnitedStatesOfAmericaScienceFictionEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_science_fiction_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaScienceEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_science_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSelfImprovement(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_self_improvement'


class ApplePodcastsUnitedStatesOfAmericaSelfImprovementEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_self_improvement_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSexuality(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_sexuality'


class ApplePodcastsUnitedStatesOfAmericaSexualityEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_sexuality_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSoccer(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_soccer'


class ApplePodcastsUnitedStatesOfAmericaSoccerEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_soccer_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSocialSciences(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_social_sciences'


class ApplePodcastsUnitedStatesOfAmericaSocialSciencesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_social_sciences_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSpirituality(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_spirituality'


class ApplePodcastsUnitedStatesOfAmericaSpiritualityEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_spirituality_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_sports'


class ApplePodcastsUnitedStatesOfAmericaSportsNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_sports_news'


class ApplePodcastsUnitedStatesOfAmericaSportsNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_sports_news_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSportsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_sports_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaStandUp(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_stand_up'


class ApplePodcastsUnitedStatesOfAmericaStandUpEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_stand_up_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaStoriesForKids(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_stories_for_kids'


class ApplePodcastsUnitedStatesOfAmericaStoriesForKidsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_stories_for_kids_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaSwimming(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_swimming'


class ApplePodcastsUnitedStatesOfAmericaSwimmingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_swimming_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaTechNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_tech_news'


class ApplePodcastsUnitedStatesOfAmericaTechNewsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_tech_news_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_technology'


class ApplePodcastsUnitedStatesOfAmericaTechnologyEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_technology_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaTennis(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_tennis'


class ApplePodcastsUnitedStatesOfAmericaTennisEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_tennis_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_true_crime'


class ApplePodcastsUnitedStatesOfAmericaTrueCrimeEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_true_crime_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaTvReviews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_tv_reviews'


class ApplePodcastsUnitedStatesOfAmericaVideoGames(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_video_games'


class ApplePodcastsUnitedStatesOfAmericaVideoGamesEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_video_games_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaVisualArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_visual_arts'


class ApplePodcastsUnitedStatesOfAmericaVisualArtsEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_visual_arts_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaVolleyball(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_volleyball'


class ApplePodcastsUnitedStatesOfAmericaVolleyballEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_volleyball_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaWilderness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_wilderness'


class ApplePodcastsUnitedStatesOfAmericaWildernessEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_wilderness_—_episodes'


class ApplePodcastsUnitedStatesOfAmericaWrestling(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_wrestling'


class ApplePodcastsUnitedStatesOfAmericaWrestlingEpisodes(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)
    podcast_creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apple_podcasts_—_united_states_of_america_—_wrestling_—_episodes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SpotifyArgentinaTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_argentina_—_top_podcasts'


class SpotifyAustraliaArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_arts'


class SpotifyAustraliaBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_business'


class SpotifyAustraliaComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_comedy'


class SpotifyAustraliaEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_education'


class SpotifyAustraliaFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_fiction'


class SpotifyAustraliaHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_history'


class SpotifyAustraliaLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_leisure'


class SpotifyAustraliaMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_music'


class SpotifyAustraliaNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_news'


class SpotifyAustraliaScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_science'


class SpotifyAustraliaSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_sports'


class SpotifyAustraliaTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_technology'


class SpotifyAustraliaTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_top_podcasts'


class SpotifyAustraliaTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_australia_—_true_crime'


class SpotifyAustriaTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_austria_—_top_podcasts'


class SpotifyCanadaTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_canada_—_top_podcasts'


class SpotifyFranceTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_france_—_top_podcasts'


class SpotifyGermanyArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_arts'


class SpotifyGermanyBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_business'


class SpotifyGermanyComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_comedy'


class SpotifyGermanyEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_education'


class SpotifyGermanyFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_fiction'


class SpotifyGermanyHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_history'


class SpotifyGermanyLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_leisure'


class SpotifyGermanyMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_music'


class SpotifyGermanyNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_news'


class SpotifyGermanyScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_science'


class SpotifyGermanySports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_sports'


class SpotifyGermanyTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_technology'


class SpotifyGermanyTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_top_podcasts'


class SpotifyGermanyTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_germany_—_true_crime'


class SpotifyGreatBritainArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_arts'


class SpotifyGreatBritainBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_business'


class SpotifyGreatBritainComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_comedy'


class SpotifyGreatBritainEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_education'


class SpotifyGreatBritainFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_fiction'


class SpotifyGreatBritainHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_history'


class SpotifyGreatBritainLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_leisure'


class SpotifyGreatBritainMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_music'


class SpotifyGreatBritainNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_news'


class SpotifyGreatBritainScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_science'


class SpotifyGreatBritainSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_sports'


class SpotifyGreatBritainTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_technology'


class SpotifyGreatBritainTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_top_podcasts'


class SpotifyGreatBritainTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_great_britain_—_true_crime'


class SpotifyItalyTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_italy_—_top_podcasts'


class SpotifyPolandTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_poland_—_top_podcasts'


class SpotifySwedenArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_arts'


class SpotifySwedenBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_business'


class SpotifySwedenComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_comedy'


class SpotifySwedenEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_education'


class SpotifySwedenFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_fiction'


class SpotifySwedenHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_history'


class SpotifySwedenLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_leisure'


class SpotifySwedenMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_music'


class SpotifySwedenNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_news'


class SpotifySwedenScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_science'


class SpotifySwedenSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_sports'


class SpotifySwedenTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_technology'


class SpotifySwedenTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_top_podcasts'


class SpotifySwedenTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_sweden_—_true_crime'


class SpotifyUnitedStatesOfAmericaArts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_arts'


class SpotifyUnitedStatesOfAmericaBusiness(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_business'


class SpotifyUnitedStatesOfAmericaComedy(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_comedy'


class SpotifyUnitedStatesOfAmericaEducation(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_education'


class SpotifyUnitedStatesOfAmericaFiction(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_fiction'


class SpotifyUnitedStatesOfAmericaHistory(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_history'


class SpotifyUnitedStatesOfAmericaLeisure(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_leisure'


class SpotifyUnitedStatesOfAmericaMusic(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_music'


class SpotifyUnitedStatesOfAmericaNews(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_news'


class SpotifyUnitedStatesOfAmericaScience(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_science'


class SpotifyUnitedStatesOfAmericaSports(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_sports'


class SpotifyUnitedStatesOfAmericaTechnology(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_technology'


class SpotifyUnitedStatesOfAmericaTopPodcasts(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_top_podcasts'


class SpotifyUnitedStatesOfAmericaTrueCrime(models.Model):
    podcast_name = models.TextField()
    podcast_link = models.TextField()
    podcast_artwork = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spotify_—_united_states_of_america_—_true_crime'

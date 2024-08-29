from rest_framework import serializers
from .models import *

class ApplePodcastsAustraliaAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaSportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaSportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaSportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaSportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceSportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceSportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanySportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanySportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAfterShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAfterShows
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAlternativeHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAlternativeHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAlternativeHealthEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAlternativeHealthEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAstronomySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAstronomy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAstronomyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAstronomyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAutomotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAutomotive
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAutomotiveEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAutomotiveEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAviation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAviationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAviationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBaseballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBaseball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBaseballEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBaseballEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBasketballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBasketball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBasketballEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBasketballEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBooks
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBooksEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBooksEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBuddhismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBuddhism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBuddhismEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBuddhismEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBusinessNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBusinessNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBusinessNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBusinessNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCareers
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCareersEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCareersEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainChemistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainChemistry
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainChemistryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainChemistryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainChristianitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainChristianity
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainChristianityEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainChristianityEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyInterviewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyInterviewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCourses
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCoursesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCoursesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCrafts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCraftsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCraftsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCricket
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDailyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDailyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDailyNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDailyNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDesign
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDesignEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDesignEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDocumentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDocumentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDocumentaryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDocumentaryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDrama
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDramaEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDramaEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEarthSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEarthSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEducationForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEducationForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEducationForKidsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEducationForKidsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEntertainmentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEntertainmentNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEntertainmentNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEntertainmentNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEntrepreneurshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEntrepreneurship
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEntrepreneurshipEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEntrepreneurshipEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFantasySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFantasySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFilmHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFilmHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFilmInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFilmInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFilmReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFilmReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFitness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFitnessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFitnessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFood
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFoodEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFoodEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFootball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainGolfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainGolf
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHinduismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHinduism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHobbies
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHobbiesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHobbiesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHockey
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHowToSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHowTo
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHowToEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHowToEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainImprovSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainImprov
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainImprovEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainImprovEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainInvestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainInvesting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainInvestingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainInvestingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainIslamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainIslam
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainIslamEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainIslamEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainJudaismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainJudaism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainJudaismEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainJudaismEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLanguageLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLanguageLearning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLanguageLearningEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLanguageLearningEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLifeSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLifeSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLifeSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLifeSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainManagement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainManagementEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainManagementEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMarketing
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMarketingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMarketingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMathematicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMathematics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMathematicsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMathematicsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMedicine
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMedicineEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMedicineEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMentalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMentalHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMentalHealthEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMentalHealthEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicCommentaryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicCommentaryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicInterviewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicInterviewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNaturalSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNaturalSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNaturalSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNaturalSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNature
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNewsCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNewsCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNewsCommentaryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNewsCommentaryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNonProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNonProfit
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNonProfitEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNonProfitEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNutrition
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNutritionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNutritionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainParentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainParenting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainParentingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainParentingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPerformingArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPerformingArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPerformingArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPerformingArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPersonalJournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPersonalJournals
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPersonalJournalsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPersonalJournalsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPhilosophy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPhysicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPhysics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPhysicsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPhysicsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPolitics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPoliticsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPoliticsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainRelationships
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainRelationshipsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainRelationshipsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainReligion
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainReligionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainReligionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainRugbySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainRugby
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainRunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainRunning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainScienceFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainScienceFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainScienceFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainScienceFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSelfImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSelfImprovement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSelfImprovementEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSelfImprovementEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSexualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSexuality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSexualityEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSexualityEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSoccerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSoccer
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSocialSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSocialSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSocialSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSocialSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSpiritualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSpirituality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSportsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSportsNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSportsNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSportsNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainStandUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainStandUp
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainStandUpEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainStandUpEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainStoriesForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainStoriesForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainStoriesForKidsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainStoriesForKidsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSwimmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSwimming
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTechNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTechNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTechNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTechNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTennisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTennis
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTvReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTvReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVideoGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVideoGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVideoGamesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVideoGamesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVisualArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVisualArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVisualArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVisualArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVolleyballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVolleyball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainWildernessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainWilderness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainWrestlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainWrestling
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalySportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalySportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAfterShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAfterShows
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAfterShowsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAfterShowsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAllPodcastsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAllPodcastsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAlternativeHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAlternativeHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAlternativeHealthEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAlternativeHealthEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAstronomySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAstronomy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAstronomyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAstronomyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAutomotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAutomotive
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAutomotiveEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAutomotiveEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAviation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAviationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAviationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBaseballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBaseball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBaseballEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBaseballEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBasketballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBasketball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBasketballEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBasketballEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBooks
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBooksEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBooksEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBuddhismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBuddhism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBuddhismEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBuddhismEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBusinessNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBusinessNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBusinessNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBusinessNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBusinessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBusinessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCareers
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCareersEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCareersEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaChemistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaChemistry
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaChemistryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaChemistryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaChristianitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaChristianity
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaChristianityEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaChristianityEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyInterviewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyInterviewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCourses
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCoursesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCoursesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCrafts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCraftsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCraftsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCricket
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCricketEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCricketEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDailyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDailyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDailyNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDailyNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDesign
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDesignEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDesignEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDocumentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDocumentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDocumentaryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDocumentaryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDrama
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDramaEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDramaEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEarthSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEarthSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEarthSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEarthSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEducationForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEducationForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEducationForKidsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEducationForKidsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEducationEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEducationEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEntertainmentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEntertainmentNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEntertainmentNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEntertainmentNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEntrepreneurshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEntrepreneurship
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEntrepreneurshipEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEntrepreneurshipEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFantasySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFantasySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFantasySportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFantasySportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmInterviewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmInterviewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFitness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFitnessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFitnessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFood
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFoodEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFoodEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFootball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFootballEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFootballEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGamesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGamesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGolfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGolf
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGolfEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGolfEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGovernmentEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGovernmentEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHinduismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHinduism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHinduismEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHinduismEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHobbies
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHobbiesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHobbiesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHockey
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHockeyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHockeyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHowToSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHowTo
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHowToEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHowToEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaImprovSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaImprov
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaImprovEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaImprovEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaInvestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaInvesting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaInvestingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaInvestingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaIslamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaIslam
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaIslamEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaIslamEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaJudaismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaJudaism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaJudaismEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaJudaismEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLanguageLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLanguageLearning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLanguageLearningEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLanguageLearningEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLeisureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLeisureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLifeSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLifeSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLifeSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLifeSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaManagement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaManagementEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaManagementEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMarketing
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMarketingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMarketingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMathematicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMathematics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMathematicsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMathematicsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMedicine
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMedicineEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMedicineEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMentalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMentalHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMentalHealthEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMentalHealthEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicCommentaryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicCommentaryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicHistoryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicHistoryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicInterviewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicInterviewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNaturalSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNaturalSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNaturalSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNaturalSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNature
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNatureEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNatureEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNewsCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNewsCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNewsCommentaryEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNewsCommentaryEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNonProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNonProfit
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNonProfitEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNonProfitEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNutrition
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNutritionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNutritionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaParentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaParenting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaParentingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaParentingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPerformingArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPerformingArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPerformingArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPerformingArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPersonalJournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPersonalJournals
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPersonalJournalsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPersonalJournalsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPhilosophy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPhilosophyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPhilosophyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPhysicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPhysics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPhysicsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPhysicsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPolitics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPoliticsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPoliticsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRelationships
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRelationshipsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRelationshipsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaReligion
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaReligionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaReligionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRugbySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRugby
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRugbyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRugbyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRunning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRunningEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRunningEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaScienceFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaScienceFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaScienceFictionEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaScienceFictionEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaScienceEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaScienceEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSelfImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSelfImprovement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSelfImprovementEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSelfImprovementEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSexualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSexuality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSexualityEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSexualityEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSoccerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSoccer
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSoccerEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSoccerEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSocialSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSocialSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSocialSciencesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSocialSciencesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSpiritualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSpirituality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSpiritualityEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSpiritualityEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSportsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSportsNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSportsNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSportsNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSportsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSportsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaStandUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaStandUp
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaStandUpEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaStandUpEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaStoriesForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaStoriesForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaStoriesForKidsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaStoriesForKidsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSwimmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSwimming
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSwimmingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSwimmingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTechNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTechNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTechNewsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTechNewsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTechnologyEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTechnologyEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTennisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTennis
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTennisEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTennisEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTrueCrimeEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTrueCrimeEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTvReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTvReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVideoGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVideoGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVideoGamesEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVideoGamesEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVisualArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVisualArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVisualArtsEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVisualArtsEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVolleyballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVolleyball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVolleyballEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVolleyballEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaWildernessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaWilderness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaWildernessEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaWildernessEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaWrestlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaWrestling
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaWrestlingEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaWrestlingEpisodes
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = ['authgrouppermissions', 'authusergroups', 'name']

class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = ['group', 'permission']

class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = ['authgrouppermissions', 'authuseruserpermissions', 'content_type', 'codename', 'name']

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['authusergroups', 'authuseruserpermissions', 'djangoadminlog', 'password', 'last_login', 'is_superuser', 'username', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'first_name']

class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = ['user', 'group']

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = ['user', 'permission']

class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = ['object_id', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user', 'action_time']

class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = ['authpermission', 'djangoadminlog', 'app_label', 'model']

class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = ['app', 'name', 'applied']

class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = ['session_key', 'session_data', 'expire_date']

class SpotifyArgentinaTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyArgentinaTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustraliaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustraliaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyAustriaTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAustriaTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyCanadaTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyCanadaTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyFranceTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyFranceTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGermanyTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGermanyTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyGreatBritainTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyGreatBritainTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyItalyTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyItalyTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyPolandTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyPolandTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifySwedenTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifySwedenTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaTopPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaTopPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']

class SpotifyUnitedStatesOfAmericaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyUnitedStatesOfAmericaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork']


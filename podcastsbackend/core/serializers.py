from rest_framework import serializers
from .models import *

class ApplePodcastsAustraliaAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsAustraliaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsAustraliaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsCanadaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsCanadaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsFranceTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsFranceTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGermanyTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGermanyTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAfterShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAfterShows
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAlternativeHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAlternativeHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAstronomySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAstronomy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAutomotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAutomotive
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainAviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainAviation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBaseballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBaseball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBasketballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBasketball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBooks
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBuddhismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBuddhism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainBusinessNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainBusinessNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCareers
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainChemistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainChemistry
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainChristianitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainChristianity
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainComedyInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainComedyInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCourses
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCrafts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainCricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainCricket
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDailyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDailyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDesign
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDocumentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDocumentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainDramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainDrama
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

class ApplePodcastsGreatBritainEntertainmentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEntertainmentNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainEntrepreneurshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainEntrepreneurship
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFantasySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFantasySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFiction
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

class ApplePodcastsGreatBritainFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainFood
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

class ApplePodcastsGreatBritainHinduismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHinduism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHobbies
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHockey
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainHowToSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainHowTo
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainImprovSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainImprov
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainInvestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainInvesting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainIslamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainIslam
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainJudaismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainJudaism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLanguageLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLanguageLearning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainLifeSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainLifeSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainManagement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMarketing
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMathematicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMathematics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMedicine
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMentalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMentalHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainMusicInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainMusicInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNaturalSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNaturalSciences
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

class ApplePodcastsGreatBritainNonProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNonProfit
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainNutrition
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainParentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainParenting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPerformingArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPerformingArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPersonalJournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPersonalJournals
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPhilosophy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPhysicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPhysics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainPolitics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainRelationships
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainReligion
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

class ApplePodcastsGreatBritainSelfImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSelfImprovement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSexualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSexuality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSoccerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSoccer
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSocialSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSocialSciences
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

class ApplePodcastsGreatBritainStandUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainStandUp
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainStoriesForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainStoriesForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainSwimmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainSwimming
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTechNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTechNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTennisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTennis
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainTvReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainTvReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVideoGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVideoGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsGreatBritainVisualArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsGreatBritainVisualArts
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

class ApplePodcastsItalyArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsItalyTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsItalyTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAfterShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAfterShows
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAllPodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAllPodcasts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAlternativeHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAlternativeHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAstronomySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAstronomy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAutomotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAutomotive
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaAviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaAviation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBaseballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBaseball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBasketballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBasketball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBooks
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBuddhismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBuddhism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBusiness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaBusinessNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaBusinessNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCareers
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaChemistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaChemistry
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaChristianitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaChristianity
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaComedyInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaComedyInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCourses
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCrafts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaCricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaCricket
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDailyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDailyNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDesign
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDocumentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDocumentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaDramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaDrama
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEarthSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEarthSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEducation
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEducationForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEducationForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEntertainmentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEntertainmentNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaEntrepreneurshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaEntrepreneurship
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFantasySportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFantasySports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFilmReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFilmReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFitness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFood
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaFootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaFootball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGolfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGolf
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaGovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaGovernment
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHinduismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHinduism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHobbies
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHockey
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaHowToSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaHowTo
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaImprovSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaImprov
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaInvestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaInvesting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaIslamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaIslam
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaJudaismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaJudaism
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLanguageLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLanguageLearning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLeisure
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaLifeSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaLifeSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaManagement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMarketing
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMathematicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMathematics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMedicine
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMentalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMentalHealth
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusic
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicHistory
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaMusicInterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaMusicInterviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNaturalSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNaturalSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNature
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNewsCommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNewsCommentary
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNonProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNonProfit
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaNutrition
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaParentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaParenting
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPerformingArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPerformingArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPersonalJournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPersonalJournals
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPhilosophy
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPhysicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPhysics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaPolitics
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRelationships
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaReligion
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRugbySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRugby
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaRunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaRunning
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaScience
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaScienceFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaScienceFiction
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSelfImprovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSelfImprovement
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSexualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSexuality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSoccerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSoccer
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSocialSciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSocialSciences
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSpiritualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSpirituality
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSports
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSportsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSportsNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaStandUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaStandUp
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaStoriesForKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaStoriesForKids
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaSwimmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaSwimming
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTechNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTechNews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTechnology
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTennisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTennis
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTrueCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTrueCrime
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaTvReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaTvReviews
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVideoGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVideoGames
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVisualArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVisualArts
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaVolleyballSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaVolleyball
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaWildernessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaWilderness
        fields = ['podcast_name', 'podcast_link', 'podcast_artwork', 'podcast_creator']

class ApplePodcastsUnitedStatesOfAmericaWrestlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplePodcastsUnitedStatesOfAmericaWrestling
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



class AggregatedArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedArts
        fields = ['data']
class AggregatedBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedBusiness
        fields = ['data']
class AggregatedComedySerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedComedy
        fields = ['data']
class AggregatedPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedPolitics
        fields = ['data']

class AggregatedHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedHistory
        fields = ['data']
class AggregatedScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedScience
        fields = ['data']
class AggregatedReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedReligion
        fields = ['data']
class AggregatedLeisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedLeisure
        fields = ['data']
class AggregatedSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedSports
        fields = ['data']
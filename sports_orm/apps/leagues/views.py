from django.shortcuts import render, redirect
from django.db.models import Q

from .models import League, Team, Player

from . import team_maker

# def index(request):
# 	context = {
# 		"leagues": League.objects.all(),
# 		"teams": Team.objects.all(),
# 		"players": Player.objects.all(),
# 	}
# 	return render(request, "leagues/index.html", context)

def index(request):
	# all baseball leagues
	league_1 = League.objects.filter(name__contains="Baseball")

	# all womens' leagues
	league_2 = League.objects.filter(name__contains="Women")

	# all leagues where sport is any type of hockey
	league_3 = League.objects.filter(sport__contains="hockey")

	# all leagues where sport is something OTHER THAN football
	league_4 = League.objects.exclude(sport__contains="football")

	# all leagues that call themselves "conferences"
	league_5 = League.objects.filter(name__contains="conference")

	# all leagues in the Atlantic region
	league_6 = League.objects.filter(name__contains="Atlantic")

	# all teams based in Dallas
	team_1 = Team.objects.filter(location="Dallas")

	# all teams named the Raptors
	team_2 = Team.objects.filter(team_name="Raptors")

	# all teams whose location includes "City"
	team_3 = Team.objects.filter(location__contains="City")

	# all teams whose names begin with "T"
	team_4 = Team.objects.filter(team_name__startswith="T")

	# all teams ordered alphabetically by location
	team_5 = Team.objects.all().order_by("location")

	# all teams ordered by team name in reverse alphabetical order
	team_6 = Team.objects.all().order_by("-team_name")

	# every player with last name "Cooper"
	player_1 = Player.objects.filter(last_name="Cooper")

	# every player with first name "Joshua"
	player_2 = Player.objects.filter(first_name="Joshua")

	# every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
	player_3 = Player.objects.filter(Q(last_name="Cooper") & ~Q(first_name="Joshua"))

	# all players with first name "Alexander" OR first name "Wyatt"
	player_4 = Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))

	context = {
		"league_1": league_1,
		"league_2": league_2,
		"league_3": league_3,
		"league_4": league_4,
		"league_5": league_5,
		"league_6": league_6,
		"team_1": team_1,
		"team_2": team_2,
		"team_3": team_3,
		"team_4": team_4,
		"team_5": team_5,
		"team_6": team_6,
		"player_1": player_1,
		"player_2": player_2,
		"player_3": player_3,
		"player_4": player_4,
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")


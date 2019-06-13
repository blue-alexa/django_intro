from itertools import filterfalse
from django.shortcuts import render, redirect
from django.db.models import Q, Count
from .models import League, Team, Player

from . import team_maker

def index(request):
	# all teams in the Atlantic Soccer Conference
	teams_1 = Team.objects.filter(league__name="Atlantic Soccer Conference")

	# all (current) players on the Boston Penguins
	players_1 = Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins")

	# all (current) players in the International Collegiate Baseball Conference
	players_2 = Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference")

	# all (current) player in the American Conference of Amateur Football with last name "Lopez"
	players_3 = Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez")

	# all football players
	players_4 = Player.objects.filter(curr_team__league__sport__contains="football")

	# all teams with a (current) player named "Sophia"
	teams_2 = Team.objects.filter(curr_players__first_name="Sophia")

	# all leagues with a (current) player named "Sophia"
	leagues_1 = League.objects.filter(teams__curr_players__first_name="Sophia")

	# everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
	players_5 = Player.objects.filter(Q(last_name="Flores") &\
									  ~Q(curr_team__location="Washington", curr_team__team_name="Roughriders"))

	# all teams, past and present, that Samuel Evans has played with
	teams_3 = Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans")

	# all players, past and present, with the Manitoba Tiger-Cats
	players_6 = Player.objects.filter(Q(curr_team__team_name="Tiger-Cats", curr_team__location="Manitoba") | \
						  Q(all_teams__team_name="Tiger-Cats", all_teams__location="Manitoba"))

	# all players who were formerly (but aren't currently) with the Wichita Vikings
	players_7 = Player.objects.filter(~Q(curr_team__team_name="Vikings", curr_team__location="Wichita") & \
						  Q(all_teams__team_name="Vikings", all_teams__location="Wichita"))

	# every team that Jacob Gray played for before he joined the Oregon Colts

	player = Player.objects.get(first_name="Jacob", last_name="Gray")
	q_all = player.all_teams.all()
	curr_id = player.curr_team.id
	teams_4 = filterfalse(lambda x: x.id == curr_id, q_all)

	teams_5 = Team.objects.filter(~Q(curr_players__first_name="Jacob", curr_players__last_name="Gray") & \
						Q(all_players__first_name="Jacob", all_players__last_name="Gray"))

	# everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
	players_8 = Player.objects.filter(Q(first_name="Joshua") & \
							(Q(curr_team__league__name="Atlantic Federation of Amateur Baseball Players") | \
							   Q(all_teams__league__name="Atlantic Federation of Amateur Baseball Players")))

	# all teams that have had 12 or more players, past and present. (Use Django annotate function.)
	teams_6 = Team.objects.annotate(num_players=Count("all_players")).filter(num_players__gte=12)

	# all players and count of teams played for, sorted by the number of teams they've played for.
	players_9 = Player.objects.annotate(num_teams=Count("all_teams")).order_by("-num_teams")

	context = {
		"teams_1": teams_1,
		"teams_2": teams_2,
		"teams_3": teams_3,
		"teams_4": teams_4,
		"teams_5": teams_5,
		"teams_6": teams_6,
		"players_1": players_1,
		"players_2": players_2,
		"players_3": players_3,
		"players_4": players_4,
		"players_5": players_5,
		"players_6": players_6,
		"players_7": players_7,
		"players_8": players_8,
		"players_9": players_9,
		"leagues_1": leagues_1,
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
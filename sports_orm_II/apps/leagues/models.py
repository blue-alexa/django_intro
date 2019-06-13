from django.db import models

class League(models.Model):
	name = models.CharField(max_length=50)
	sport = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return "League name: %s, sport: %s"%(self.name, self.sport)

class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)
	league = models.ForeignKey(League, related_name="teams")

	def __repr__(self):
		return "Team location: %s, name: %s, league: %s" % (self.location, self.team_name, self.league.name)

class Player(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	curr_team = models.ForeignKey(Team, related_name="curr_players")
	all_teams = models.ManyToManyField(Team, related_name="all_players")

	def __repr__(self):
		return "Player %s, %s team: %s" % (self.first_name, self.last_name, self.curr_team.team_name)

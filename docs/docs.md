# bits and bops

1. make buttons on group card nicer (maybe take out background change on hover)
2. remember! get it working and you can update design after a beta version is out

# thought dump 

1. add some indiication of time on the cirular day stats
2. make the pop up for circular day stat be cooler like a unfurl from a small top right arc
# restructure

1. Shift each calender cell into it's own component (getting too complex)

# functionality

1. make group
2. join group (via link [not search])
3. leave group (if group empty kill it) (if 1 person suggest join link)
4. update availability
5. lock in event (keep track of events so you can remove the times from availability + show stats)
6. dashboard showing upcoming events / groups
7. group creator should be able to kill a group

# Pages

#### Navbar

1. log out
2. logo

#### dashboard

1. Join group
2. Make group
3. Upcomming events
4. previous events
5. go to group
6. update availability

#### group

1. members
2. heatmap
3. top 3 times
4. update availability
5. make event at given time
6. previous events in group
7. group name
8. circle around profile pictures who's color indicates how available they are for a certain time
9. on hover on a spot on the heatmap, greys out everyone who can't make it / updates colour around each profile depending on green orange yellow red etc.

#### event

1. make event (modal)
2. see event (small div / component + modal with info which pops up on click)
3. [stretch goal] have events from fb

#### Update Availability

1. Modal.
2. week by week view (left and right buttons to make a api request)
3. click to set
4. submit and update on confirmation

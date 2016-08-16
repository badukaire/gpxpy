
import gpxpy
import gpxpy.gpx

def dispTracks() :
  liTrack = 0
  for lTrack in gXmlGPX.tracks:
    liTrack += 1
    print "============="
    print "track #%d name:%s:" % ( liTrack, lTrack.name )
    liSegment = 0
    for lSegment in lTrack.segments:
      liSegment += 1
      print "--"
      print "segment #%d, track #%d" % ( liSegment, liTrack )
      for lPoint in lSegment.points:
        print "Point at ({0},{1}) -> {2}".format( lPoint.latitude, lPoint.longitude, lPoint.elevation )
        print "-- timestamp:%s:" % lPoint.time
      print "end of segment #%d, lTrack #%d" % ( liSegment, liTrack )
      print "----"
    print "end of track #%d" % ( liTrack )
    print "--------"
    print ""

def dispWaypoints() :
  liWaypt = 0
  for lWaypoint in gXmlGPX.waypoints:
    liWaypt += 1
    print "============="
    print "waypoint #%d" % ( liWaypt )
    print "waypoint {0} -> ({1},{2})".format( lWaypoint.name, lWaypoint.latitude, lWaypoint.longitude )
    print "-- comment:", lWaypoint.comment
    print "-- description:", lWaypoint.description
    print "-- symbol:", lWaypoint.symbol
    
def dispRoutes() :
  liRoute = 0
  for lRoute in gXmlGPX.routes:
    liRoute += 1
    print "============="
    print "Route: #%d" % ( liRoute )
    for lPoint in lRoute.points:
      print "Point at ({0},{1}) -> {2}".format( lPoint.latitude, lPoint.longitude, lPoint.elevation )
      print "-- timestamp:%s:" % lPoint.time


# Parsing an existing file:
# -------------------------

lsFileGPX = "test_files/cerknicko-jezero.gpx"
lFileGPX = open( lsFileGPX, "r" )

gXmlGPX = gpxpy.parse( lFileGPX )

dispTracks()
#dispWaypoints()
dispRoutes()


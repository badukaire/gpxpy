import sys
import getopt

# local dir imports
import gpxpy
import gpxpy.gpx


def eprint( sErrorMsg ) :
  sys.stderr.write( sErrorMsg )
  sys.stderr.write( "\n" )


def usage() :
  print "options :"
  print "* -h : display this help text"
  print "* -d <displayWhat>: what to display"
  print "  <displayWhat> can be: routes, waypoints, tracks"
  print "* -n <displayWhich>: which one to display (number starting by 1)"


def checkOptions( pListParams ) :

  global gsFileGPX
  print( "checkOptions, args:", pListParams )
  try:
    lOptList, lList = getopt.getopt( pListParams, 'n:d:h' )

  except getopt.GetoptError:
    eprint( "FATAL : error analyzing command line options" )
    eprint( "" )
    usage()
    sys.exit( 1 )

  # TODO : use shift / setenv --

  #print( lOptList )
  #print( lList )
  for lOpt in lOptList :
    #print( "lOpt :" + str( lOpt ) )
    if lOpt[0] == '-h' :
      usage()
      sys.exit( 0 )
    if lOpt[0] == "-n" :
      lsVal = lOpt[1]
      try :
        liVal = int( lsVal )
      except :
        eprint( "FATAL: %s not a valid number" % lsVal )
        usage()
        sys.exit( 1 )
      if liVal > 0 :
        global giWhich
        giWhich = liVal
      else :
        eprint( "FATAL: %d must be >= 1" % liVal )
        usage()
        sys.exit( 1 )
    if lOpt[0] == "-d" :
      lsVal = lOpt[1]
      if lsVal == "waypoints" :
        global gbDispWaypts
        gbDispWaypts = True
      elif lsVal == "tracks" :
        global gbDispTracks
        gbDispTracks = True
      elif lsVal == "routes" :
        global gbDispRoutes
        gbDispRoutes = True
      else :
        eprint( "FATAL: Invalid item to display %s" % lsVal )
        eprint( "==========" )
        usage()
        sys.exit( 1 )

  print "lList => ", lList
  if len( lList ) > 0 :
    gsFileGPX = lList[ 0 ]
    print "will read file %s" % gsFileGPX


def dispPoint( pPoint ) :
  print "Point at ({0},{1}) -> {2}".format( pPoint.latitude, pPoint.longitude, pPoint.elevation )
  print "-- timestamp:%s:" % pPoint.time


def dispTracks() :
  liTrack = 0
  for lTrack in gXmlGPX.tracks:
    liTrack += 1
    if giWhich > 0 :
      print "giWhich = %d" % giWhich
      if not liTrack == giWhich :
        print "skip track #%d" % liTrack
        continue
    print "============="
    print "track #%d name:%s:" % ( liTrack, lTrack.name )
    liSegment = 0
    for lSegment in lTrack.segments:
      liSegment += 1
      print "--"
      print "segment #%d, track #%d" % ( liSegment, liTrack )
      for lPoint in lSegment.points:
        dispPoint( lPoint )
      print "end of segment #%d, lTrack #%d" % ( liSegment, liTrack )
      print "----"
    print "end of track #%d" % ( liTrack )
    print "--------"
    print ""


def dispWaypts() :
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
      dispPoint( lPoint )


gbDispTracks = False
gbDispWaypts = False
gbDispRoutes = False
giWhich = 0

liArgs = len( sys.argv )
if liArgs > 1 :
  gsFileGPX = None
  checkOptions( sys.argv[ 1 : ] )
  if not gsFileGPX == None :
    lFileGPX = open( gsFileGPX, "r" )
  else :
    eprint( "NO GPX file provided, will use stdin" )
    lFileGPX = sys.stdin
else : # stdin
  lFileGPX = sys.stdin
  gbDispTracks = True
  gbDispWaypts = True
  gbDispRoutes = True


try :
  gXmlGPX = gpxpy.parse( lFileGPX )
  lFileGPX.close()

except :
  eprint( "FATAL: Error parsing GPX data" )
  sys.exit( 1 )

if gbDispTracks == False and gbDispWaypts == False and gbDispRoutes == False :
  print "NOT displaying anything"
if gbDispTracks == True :
  print "================"
  print "display Tracks ..."
  dispTracks()
  print ""
  print "Tracks displayed"
  print "================"
  print ""
if gbDispWaypts == True :
  print "================"
  print "display Waypts ..."
  dispWaypts()
  print ""
  print "Waypts displayed"
  print "================"
  print ""
if gbDispRoutes == True :
  print "================"
  print "display Routes ..."
  dispRoutes()
  print ""
  print "Routes displayed"
  print "================"
  print ""


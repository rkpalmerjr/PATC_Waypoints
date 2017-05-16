import os
import gpxpy
import gpxpy.gpx

# Parsing an existing file:
# ----------------------

rootdir = r'[RootFolder]'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        extension = os.path.splitext(file)[1][1:]

        # if extension == "gpx":
        if extension == "gpx" and file[10:12] == "W_":
            gpx_file = os.path.join(subdir, file)
            print gpx_file

            gpx_file = open(gpx_file, 'r')

            gpx = gpxpy.parse(gpx_file)
            for waypoint in gpx.waypoints:
                print '{0} -> ({1},{2})'.format(waypoint.name,
                                                waypoint.latitude,
                                                waypoint.longitude)

'''
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        print 'Point at ({0},{1}) -> {2}'.format(point.latitude,
                                                                 point.longitude,
                                                                 point.elevation)

            for route in gpx.routes:
                print 'Route:'
                for point in route.points:
                    print 'Point at ({0},{1}) -> {2}'.format(point.latitude,
                                                             point.longitude,
                                                             point.elevation)

            # There are many more utility methods and functions:
            # You can manipulate/add/remove tracks, segments, points, waypoints and routes and
            # get the GPX XML file from the resulting object:
 '''

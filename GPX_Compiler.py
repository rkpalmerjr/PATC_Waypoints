import os
import gpxpy
import gpxpy.gpx
import csv

# Parsing an existing file:
# ----------------------

rootdir = raw_input("Enter the path to the directory containing GPX files:")

count = 0
csv_out = raw_input("Enter the FULL directory including the name of the csv file where you want to put the output csv file at:")

with open(csv_out, 'wb') as csvfile:
    writer = csv.writer(csvfile)

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:

            extension = os.path.splitext(file)[1][1:]

            # if extension == "gpx":
            if extension == "gpx" and file[10:12] == "W_":

                gpx_file = os.path.join(subdir, file)
                #print gpx_file

                gpx_file_obj = open(gpx_file, 'r')

                gpx = gpxpy.parse(gpx_file_obj)

                for waypoint in gpx.waypoints:

                    count += 1
                    print count

                    print '{1},{2},{3},{0}'.format(waypoint.name,
                                                    waypoint.latitude,
                                                    waypoint.longitude,
                                                    waypoint.elevation) + \
                                                    "," + file

                    # Write the first row of the output file as headers for the three columns
                    writer.writerow((waypoint.name, waypoint.latitude, waypoint.longitude, waypoint.elevation, file))

# This was in example from internet but not used here.
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


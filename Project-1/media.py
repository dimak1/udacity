"""
File:     media.py
Course:   Udacity Full-Stack Developer Nanodegree
Project:  Movies Website
Author:   Dima K
Date:     Aug 2017
"""

import webbrowser


class Movie():
    """
        Movie class to represent each Movie on the website.
        It consists of a Title, Year, Storyline, Image and Trailer.
    """

    # Constructor method to initialize the Movie class
    def __init__(self, title, year, storyline, image, trailer):
        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    # Open trailer for a movie
    def show_trailer(self):
        webbrowser.open(self.trailer)

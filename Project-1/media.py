"""
File:     media.py
Course:   Udacity Full-Stack Developer Nanodegree
Project:  Movies Website
Author:   Dima K
Date:     Aug 2017
"""

import webbrowser


class Movie():
    """Movie class to construct movie objects"""

    def __init__(self, title, year, storyline, image, trailer):
        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)

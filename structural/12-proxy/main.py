from abc import ABC, abstractmethod
from typing import List

class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def listVideos(self):
        pass

    @abstractmethod
    def getVideoInfo(self, video_id):
        pass

    @abstractmethod
    def downloadVideo(self, video_id):
        pass

# The concrete implementation of a service connector. Methods of this class can
# request information from YouTube. The speed of the request depends on a
# user's internet connection as well as YouTube's. The application will slow down
# if a lot of requests are fired at the same time, even if they all request the
# same information.
class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):
    def listVideos(self):
        return "Sending and API request to Youtube"

    def getVideoInfo(self, video_id):
        return f"Getting metadata about {video_id}"

    def downloadVideo(self, video_id):
        return f"Downloading {video_id}"


# To save some bandwidth, we can cache request results and keep them for some time. But it may be impossible to put such code directly into the service class. For example, it could have // been provided as part of a third party library and/or defined as `final`. That's why we put the caching code into a new
# proxy class which implements the same interface as the
# service class. It delegates to the service object only when the real requests have to be sent.
class CachedYoutubeClass(ThirdPartyYoutubeLib):
    _service: ThirdPartyYoutubeLib
    _list_cache: List[str]
    _video_cache: List[str]
    _download_exists: bool
    needReset: bool

    def __init__(self, service: ThirdPartyYoutubeLib):
        self._service = service

    def listVideos(self):
        if not self._list_cache or self.needReset:
            self._list_cache = self._service.listVideos()
        return self._list_cache

    def getVideoInfo(self, video_id):
        if not self._video_cache or self.needReset:
            self._video_cache = self._service.getVideoInfo(video_id)
        return self._video_cache

    def downloadVideo(self, video_id):
        if not self._download_exists or self.needReset:
            self._downloadCache = self._service.downloadVideo(video_id)


class YoutubeManager:
    _service: ThirdPartyYoutubeLib

    def __init__(self, service: ThirdPartyYoutubeLib):
        self._service = service

    def render_video_page(self, video_id: str):
        video_info = self._service.getVideoInfo(video_id)
        return f"<html><body>{video_info}</body></html>"

    def render_list_panel(self):
        video_list = self._service.listVideos()
        return f"<html><body>{video_list}</body></html>"

    def react_on_user_input(self, video_id: str):
        self.render_video_page(video_id)
        self.render_list_panel()


class Application:
    def __init__(self):
        a_youtube_service = ThirdPartyYoutubeClass()
        a_youtube_proxy = CachedYoutubeClass(a_youtube_service)
        manager = YoutubeManager(a_youtube_proxy)
        manager.react_on_user_input("video_id")

import DaVinciResolveScript as dvr
resolve = dvr.scriptapp("Resolve")

"""
script to get all the metadata from items in a root folder (media as timelines, images ect. are considered as clips by default)

pm == project manager
proj == project
tl == timeline
"""

pm = resolve.GetProjectManager()
pm.LoadProject("RESOLVE_API_TEST")
proj = pm.GetCurrentProject()
mediapool = proj.GetMediaPool()
rootFolder = mediapool.GetRootFolder()
resolve_media_storage = resolve.GetMediaStorage()
clips = rootFolder.GetClipList()

for clip in clips:
    # from IPython import embed
    # embed()
    clip_porerties = clip.GetClipProperty()
    clipname = clip.GetName()
    print("\n" + "------------------" + "\n" +
          clipname + "\n" + "------------------")
    for key, value in clip_porerties.items():
        print(key, ':', value)

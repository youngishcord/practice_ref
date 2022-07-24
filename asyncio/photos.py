import asyncio
import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj["albumId"], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')

async def photos_by_album(task_name, album, session):
    print(f'{task_name}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]

async def main():
    async with aiohttp.ClientSession() as session:
        photos = await photos_by_album('task 1', 1, session)
        print_photo_titles(photos)

if __name__ == '__main__':
    asyncio.run(main())
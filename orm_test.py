import asyncio
import orm
from user import User
import sys
__author__ = 'victory'

async def connecDB(loop):
	username = 'ct'
	password = '123456'
	dbname = 'test'
	await orm.create_pool(loop,user=username,password=password,db=dbname)

async def destroyDB():
	await orm.destroy_pool()

async def test_findAll(loop):
	await connecDB(loop)
	userlist = await User.findAll(orderBy="name",limit=2)
	print('all user:%s' % userlist)
	await destroyDB()

async def test_findNumber(loop):
	await connecDB(loop)
	id = await User.findNumber('id')
	name = await User.findNumber('name')
	print('id:%s;name:%s' % (id,name))
	await destroyDB()

async def test_find(loop):
	await connecDB(loop)
	user = await User.find('123')
	print('user:%s' % user)
	await destroyDB()

async def test_save(loop):
	await connecDB(loop)
	# user = await User.find('123')
	# if user is None:
	user = User(id=3,name='yqh')
	await user.save()
	await destroyDB()

async def test_update(loop):
	await connecDB(loop)
	user = await User.find(1)
	if user is not None:
		user.name = 'zona'
		await user.update()
		print('user update:%s' % user)
	await destroyDB()

async def test_remove(loop):
	await connecDB(loop)
	user = await User.find(3)
	if user is not None:
		await user.remove()
		print('user remove:%s' % user)
	await destroyDB()

loop = asyncio.get_event_loop()

#loop.run_until_complete(test_findAll(loop))
#loop.run_until_complete(test_findNumber(loop))
task = [test_find(loop), test_save(loop), test_update(loop), test_remove(loop)]
# loop.run_until_complete(test_find(loop))
# loop.run_until_complete(test_save(loop))
# loop.run_until_complete(test_update(loop))
# loop.run_until_complete(test_remove(loop))
loop.run_until_complete(asyncio.wait(task))

loop.close()
# if loop.is_closed():
#     sys.exit(0)
from models import User
import asyncio
import orm
import pdb
import time


# import pdb


# 测试插入


async def test_save(loop):
    await orm.create_pool(loop, user='luyan', password='luyan', db='pyblog')
    u = User(name='test', email='hello1@example.com',
             passwd='test', image='about:blank')
    # pdb.set_trace()
    await u.save()

# 测试查询


async def test_findAll(loop):
    await orm.create_pool(loop, user='luyan', password='luyan', db='pyblog')
    # 这里给的关键字参数按照xxx='xxx'的形式给出，会自动分装成dict
    rs = await User.findAll(email='test@example.com')		# rs是一个元素为dict的list
    # pdb.set_trace()
    for i in range(len(rs)):
        print(rs[i])

# 查询条数?


async def test_findNumber(loop):
    await orm.create_pool(loop, user='luyan', password='luyan', db='pyblog')
    count = await User.findNumber('email')
    print(count)

# 根据主键查找，这里试ID


async def test_find_by_key(loop):
    await orm.create_pool(loop, user='luyan', password='luyan', db='pyblog')
    # rs是一个dict
    # ID请自己通过数据库查询
    rs = await User.find_by_key('001462842245433486d2b335863462aa80ca2bb18de33ae000')
    print(rs)

# 根据主键删除


async def test_remove(loop):
    await orm.create_pool(loop, user='luyan', password='luyan', db='pyblog')
    # 用id初始化一个实例对象
    u = User(id='001462843355235e034af503acf4113933dc6d7c2298c0d000')
    await u.remove()


# 根据主键更新
async def test_update(loop):
    await orm.create_pool(loop, user='luyan', password='luyan', db='pyblog')
    # 必须按照列的顺序来初始化：'update `users` set `created_at`=?, `passwd`=?, `image`=?,
    # `admin`=?, `name`=?, `email`=? where `id`=?' 注意这里要使用time()方法，否则会直接返回个时间戳对象，而不是float值
    u = User(id='001462843355235e034af503acf4113933dc6d7c2298c0d000', created_at=time.time(), passwd='test',
             image='about:blank', admin=True, name='test', email='hello1@example.com')  # id必须和数据库一直，其他属性可以设置成新的值,属性要全
    # pdb.set_trace()
    await u.update()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_update(loop))
__pool = orm.__pool
__pool.close()  # 需要先关闭连接池
loop.run_until_complete(__pool.wait_closed())
loop.close()

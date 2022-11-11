man = list('heloomanaboutnwhoj oueyoyaeo uehao ohfoae')
frist , *middle , last = man

record = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]

def do_foo(x,y):
    print('foo',x,y)
def do_bar(a):
    print('bar',a)

for tag, *args in record:
    if tag == 'foo':
        do_foo(*args)
    else:
        do_bar(*args)

line = 'nobody:*:-2:-2:Unpriviledged User:/var/empty:/usr/bin/false'
uname , *fields , homedir, sh = line.split(':')
print(f"{uname} \n {fields}\n {homedir}\n {sh}")
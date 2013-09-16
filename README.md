fradiusauth
===========

basic external freeradius auth example

tested against freeradius version: 2.1.10

/etc/freeradius/users

<pre><code>
DEFAULT  Auth-Type = Accept
         Exec-Program-Wait = "/usr/local/bin/fradiusauth.py %{User-Name} '%{User-Password}' %{Calling-Station-Id} %{NAS-IP-Address} %{Framed-Protocol}",
         Fall-Through = Yes

chasemp
</code></pre>

/etc/freeradius/clients.conf

<pre><code>
client 127.0.0.1 {
  secret = radsecret
  shortname = myhost
  nastype = other
}
</code></pre>


#### On the client requesting host

<pre><code>
git clone https://github.com/chasemp/py-radius.git
cd py-radius
python setup.py install
</code></pre>

OK

    libradclient.py 127.0.0.1 radsecret chasemp 1234
    chasemp authenticated

    libradclient.py 127.0.0.1 radsecret chasemp foo
    Authentication Failed

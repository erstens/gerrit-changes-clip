# gerrit-changes-clip
Gerrit's push needs review information copied to the clipboard .

### require :

* python2.x

* request

  > use `npm` to install this module .

###global.conf

* site 

  > **site = http://www.gggggg.com**

* url

  > user = jim

* append : The last additional information

  > append = @father @mum @grandfather 

* os : Use `pbcopy` in the mac `clip` in win

  > os = mac

  or

  > os = win

* auth : Manually login to the web site, using the `developer tools` to find `http-header` `Authorization`, into this field(any request)

  > auth = Basic dkimZ2FvOiuhnbbhbw==


### use

#### greivew

> copy review info to clipboard .

* In mac

```py
$ python greivew.py
```

* In win

Double click `greivew.py`.

* Last

`Ctrl + v` to paste it .

#### clone_all

> clone all projects in remote .

``` shell
$ python clone_all.py
```


# Traduir

## Roadmap

I would be happy with these for a v1

- [x] Get text on image
- [x] Translate words on image
- [x] Put translated words on the image
- [ ] Readable meme text  
  - [x] Put white under text for readability
  - [ ] Use a font suitable for memes (Black with white borders maybe?)
  - [ ] Figure out a way to put words on the same line for readability
  - [ ] Blur area under text instead of an ugly white square
- [ ] Word dictionnary
  - [ ] Ability to replace some words with common words we use
  - [ ] Let page admins edit the list, no manual update needed to apply changes
- [ ] Post to facebook
  - [ ] Post picture on a facebook page
  - [ ] Have a bank of images to post periodicaly on the page
  - [ ] Maybe read DMs and send back translated memes?

This will come later, v2 maybe

- [ ] Web interface ?
  - [ ] Let some users upload pics to translated them instantly
  - [ ] Password-protected translation API
- [ ] Archive memes
  - [ ] Keep translated memes in a user-friendly place
- [ ] Analytics
  - [ ] Keep track of text on memes and user engagement
  - [ ] Keep track of top posts
- [ ] Text improvement
  - [ ] Figure out text rotation when words are crooked
 

# Anglais (yeet)

It translate

### How to make this work

You have to install `pipenv` and do `pipenv install` and then you can just 

``` sh
pipenv run python3 src/main.py memes/en/english-meme.png fr
```

### Authentification with Google cloud

If you want this to work, you need to authenticate with Google cloud.

[follow this linkg](https://cloud.google.com/docs/authentication/getting-started#linux-or-macos) to generate your `gcloud-auth.json` 

# Francais (Lois 101)

sa tradui

### Faire rouller la patente

Installe `pipenv` et fait `pipenv install`. Après ça, fait:

``` sh
pipenv run python3 src/main.py memes/en/english-meme.png fr
```

### Authentification avec Google cloud

Pour que ça fonctionne, il faut avoir un projet Google cloud platform actif.

En gros, suis [ce lien là](https://cloud.google.com/docs/authentication/getting-started#linux-or-macos) pour générer ton fichier `gcloud-auth.json` 

a = '''느슨.달팽이.빠름.달팽이.엄격느슨.달팽이.빠름.달팽이.엄격느슨.달팽이.빠름.달팽이.엄격느슨.달팽이.빠름.달팽이.엄격느슨.달팽이.빠름.달팽이.엄격'''

a = a.replace(".", "+727")\
            .replace(",", "-3302")\
                .replace("토끼", "*")\
                    .replace("달팽이", "/")\
                        .replace("빠름", "+")\
                            .replace("느림", "-")\
                                .replace("느슨", "(")\
                                    .replace("엄격", ")")

print(a)
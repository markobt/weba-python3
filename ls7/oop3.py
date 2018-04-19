class luha():
    form = 'tolstaya'


class trenazhorny_zal:
    form = 'tolstaya'

    def hudeem(self, newform):
        self.form = newform
        return newform


luha1 = luha()
luha2 = trenazhorny_zal()

print('1 юха ', luha1.form)
print('2 юха ', luha2.form)

luha2.hudeem("Stroinaya")
luha1.form = luha2.form

print('теперь 2 юха , после тренажерки ', luha2.form)
print('теперь 1 юха тоже , после тренажерки ', luha1.form)
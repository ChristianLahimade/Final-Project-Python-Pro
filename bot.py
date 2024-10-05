import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def hitung_emisi_listrik(kwh):
    return kwh * 0.7  # kg CO₂

def hitung_emisi_transport(bahan_bakar, liter):
    if bahan_bakar.lower() == 'bensin':
        return liter * 2.31  # kg CO₂ per liter
    elif bahan_bakar.lower() == 'diesel':
        return liter * 2.68  # kg CO₂ per liter
    else:
        return None

@bot.event
async def on_ready():
    print(f'Bot telah masuk sebagai {bot.user}!')

@bot.command()
async def menu(ctx):
    embed = discord.Embed(
        title="Menu Kalkulator Emisi Gas Rumah Kaca",
        description="Berikut adalah daftar perintah yang tersedia:",
        color=0x1abc9c
    )
    embed.add_field(name="!listrik <jumlah kWh>", value="Menghitung emisi listrik berdasarkan penggunaan listrik dalam kWh.", inline=False)
    embed.add_field(name="!transport <jenis bahan bakar> <jumlah liter>", value="Menghitung emisi transportasi berdasarkan jenis bahan bakar (bensin/diesel) dan jumlah liter yang dikonsumsi.", inline=False)
    embed.add_field(name="!tips", value="Menampilkan menu tips untuk mengurangi emisi gas rumah kaca.", inline=False)
    embed.set_footer(text="Gunakan perintah ini dengan mengetikkan '!' diikuti nama perintah.")
    await ctx.send(embed=embed)


@bot.command()
async def listrik(ctx, kwh: float):
    emisi = hitung_emisi_listrik(kwh)
    embed = discord.Embed(
        title="Emisi Listrik",
        description=f"Penggunaan listrik sebesar {kwh} kWh menghasilkan emisi gas rumah kaca sebesar **{emisi:.2f} kg CO₂**.",
        color=0xf1c40f
    )
    await ctx.send(embed=embed)

@bot.command()
async def transport(ctx, bahan_bakar: str, liter: float):
    emisi = hitung_emisi_transport(bahan_bakar, liter)
    if emisi is not None:
        embed = discord.Embed(
            title="Emisi Transportasi",
            description=f"Penggunaan {liter} liter {bahan_bakar} menghasilkan emisi gas rumah kaca sebesar **{emisi:.2f} kg CO₂**.",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Jenis bahan bakar tidak dikenal. Gunakan 'bensin' atau 'diesel'.")

@bot.command()
async def tips(ctx):
    embed = discord.Embed(
        title="Menu Tips Mengurangi Emisi Gas Rumah Kaca",
        description="Pilih kategori tips berikut dengan mengetikkan perintah:\n\n"
                    "**!tipslistrik** - Mengurangi emisi dari penggunaan listrik.\n"
                    "**!tipstransportasi** - Mengurangi emisi dari transportasi.\n"
                    "**!tipssampah** - Mengurangi emisi dari pengelolaan sampah.",
        color=0x3498db
    )
    embed.set_footer(text="Pilih salah satu kategori untuk informasi lebih lanjut.")
    await ctx.send(embed=embed)

@bot.command()
async def tipslistrik(ctx):
    embed = discord.Embed(
        title="Tips Mengurangi Emisi dari Penggunaan Listrik",
        description="Berikut adalah beberapa cara yang dapat dilakukan untuk mengurangi emisi gas rumah kaca dari penggunaan listrik:",
        color=0xf39c12
    )
    tips_list = [
        "🔋 **Gunakan Lampu Hemat Energi:** Ganti lampu biasa dengan lampu LED yang lebih hemat energi.",
        "🔌 **Matikan Alat Elektronik:** Cabut alat elektronik yang tidak digunakan untuk mengurangi penggunaan daya listrik.",
        "🌞 **Manfaatkan Cahaya Alami:** Buka jendela dan gunakan cahaya alami di siang hari untuk mengurangi penggunaan lampu.",
        "📶 **Gunakan Perangkat dengan Efisiensi Energi Tinggi:** Pilih perangkat elektronik dengan label hemat energi."
    ]
    for tip in tips_list:
        embed.add_field(name="\u200B", value=tip, inline=False)
    
    embed.set_footer(text="Setiap tindakan kecil dapat membantu mengurangi emisi!")
    await ctx.send(embed=embed)

@bot.command()
async def tipstransportasi(ctx):
    embed = discord.Embed(
        title="Tips Mengurangi Emisi dari Transportasi",
        description="Berikut adalah beberapa cara yang dapat dilakukan untuk mengurangi emisi gas rumah kaca dari transportasi:",
        color=0xe74c3c
    )
    tips_list = [
        "🚶‍♂️ **Berjalan Kaki atau Bersepeda:** Gunakan jalan kaki atau sepeda untuk perjalanan singkat.",
        "🚌 **Gunakan Transportasi Umum:** Menggunakan bus atau kereta api dapat mengurangi emisi per orang dibandingkan mobil pribadi.",
        "🚗 **Berkendara Bersama:** Bagikan kendaraan dengan rekan kerja atau teman untuk mengurangi jumlah kendaraan di jalan.",
        "🔋 **Pertimbangkan Kendaraan Listrik:** Jika memungkinkan, beralih ke kendaraan listrik untuk mengurangi emisi langsung."
    ]
    for tip in tips_list:
        embed.add_field(name="\u200B", value=tip, inline=False)
    
    embed.set_footer(text="Mengurangi penggunaan kendaraan pribadi dapat membantu lingkungan!")
    await ctx.send(embed=embed)

@bot.command()
async def tipssampah(ctx):
    embed = discord.Embed(
        title="Tips Mengurangi Emisi dari Pengelolaan Sampah",
        description="Berikut adalah beberapa cara yang dapat dilakukan untuk mengurangi emisi gas rumah kaca dari pengelolaan sampah:",
        color=0x2ecc71
    )
    tips_list = [
        "♻️ **Daur Ulang:** Pisahkan sampah seperti plastik, kertas, dan logam untuk didaur ulang.",
        "📦 **Kurangi Penggunaan Barang Sekali Pakai:** Hindari penggunaan barang seperti kantong plastik, botol plastik, dan sedotan sekali pakai.",
        "🍂 **Kompos Sampah Organik:** Sampah organik seperti sisa makanan dan daun bisa dijadikan kompos untuk pupuk alami.",
        "👖 **Donasi atau Jual Barang Bekas:** Alih-alih membuang barang yang tidak terpakai, donasikan atau jual untuk digunakan kembali."
    ]
    for tip in tips_list:
        embed.add_field(name="\u200B", value=tip, inline=False)
    
    embed.set_footer(text="Pengelolaan sampah yang baik dapat mengurangi emisi metana dan polusi!")
    await ctx.send(embed=embed)
bot.run('ICIKIWIR')
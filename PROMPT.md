UPGRADE v2 news-image-20261121 (make.fun) — pola TERBUKTI cover-art v2: SATU sesi fresh top-level RAMPING yang mengarang + verifikasi + bundle + submit sekaligus. Ikuti skill makefun_bounty_submission (~/workspace/custom-skills/makefun_bounty_submission/SKILL.md) PERSIS. Perintah Imam 21 Nov 16:50 WIB: perbaiki lagi edisi news-image yang peringkatnya jelek (edisi 17 Nov terkunci/sudah diputus peringkat 5.174/7.904 — TIDAK bisa diubah; yang diperbaiki adalah edisi yang jendelanya masih buka, termasuk edisi ini).

KEADAAN: v1 edisi ini berdiri — submission 01a1fc27-b629-76db-b324-8bc1e8441d6a, kode AF-9MYBJ-PPAPK-VASM1-MKRJX, repo DLiiMaGaming/daily-orbit-20261121, hasil 7 Des 2026 08:00 UTC. LANGKAH PERTAMA: verifikasi dari kit/API apakah jendela submit edisi news-image-20261121 masih buka. Bila sudah tutup → berhenti, laporkan, v1 final. Bila masih buka → lanjut; submit ulang sah (final = submit terakhir sebelum deadline).

STANDAR JUARA (Imam 21 Nov 16:46): sebelum mengarang, baca bagian news-image di file riset juara ~/workspace/goals/make-fun-free-bounty-entries/hidden_files/makefun-winners-research-2026-11-20.md (diperbarui 21 Nov sore) dan terapkan resep juaranya — ATM pola, bukan menyalin karya. Target peringkat atas, bukan papan 10K.

ATURAN KERAS:
- SEMUA kode first-party dikarang FRESH di sesi ini. DILARANG cp dari folder versi lama; DILARANG membaca source lama. Baca hanya RULES.txt kit + ringkasan build v1 di screening-state.json (prosa) + file riset juara.
- MULAI RECORDING DULU bila kompetisi memakai sealed recording (pola skill); bila server menolak record, pakai jalur bundle/loose sesuai RULES. Jangan hapus .git folder kerja.
- Repo publik baru lewat BROWSER TASK (GitHub connector 403 untuk create_repository; jalur browser terbukti).
- Submit HANYA bila karya v2 plausibly LEBIH KUAT dari v1 menurut resep juara + verify kit. Bila tidak, JANGAN submit — laporkan, v1 tetap final.

URUTAN: verifikasi jendela → recording → baca RULES + riset juara + ringkasan v1 → karang generator fresh + karya v2 → repo via browser → bundle dari SESI INI (usage muse.db NYATA — JANGAN PERNAH memalsukan usage/transkrip/prompt-origin) → check lolos → SUBMIT (env MAKEFUN_CREDENTIALS=$HOME/.makefun/credentials-cli, header `x-api-key`) → catat ke screening-state.json submissions["news-image-20261121"] field v2_submission TANPA menimpa v1 → log ke ~/workspace/goals/make-fun-free-bounty-entries/hidden_files/makefun-news-image-20261121-v2-log.md → laporkan hasil akhir Bahasa Indonesia.

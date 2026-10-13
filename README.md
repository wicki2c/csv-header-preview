# CSV header preview

Preview the header-renaming step from the CSV Cleanup Kit before touching any CSV data. The script shows original and proposed ASCII snake_case names by position, including duplicate suffixes. Python 3.10+ only; no dependencies, account, network or file writes.

```sh
python3 csv_header_preview.py ' Client Name ' 'Client-Name' '名'
```

This fictional example proposes `client_name`, `client_name_2` and `column`. Non-Latin text, accents, punctuation and currency distinctions can be lost; compare every proposal with the original. Renaming does not prove compatibility with any receiving system. The sample accepts header strings only. It does not read CSVs, clean cells, remove duplicates, convert dates, neutralize formulas or validate financial records.

The code is a bounded sample of the existing reviewed tool's header logic, created with AI assistance and checked with fictional cases. No outcome, security or compatibility guarantee; do not pass personal/client data in a public example or support request. This is not the paid kit or a hosted service.

The optional [CSV Cleanup Kit](https://passiveexperiment.gumroad.com/l/osmloi?utm_source=github&utm_medium=sample&utm_campaign=mkt10-csv-cleanup-kit) is USD9 on Gumroad and includes the full offline cleanup script, JSON change report, fictional before/after exercise and printable Plan/Check/Handoff sheets in A4/US Letter. The paid kit retains its single-business licence; no worksheet or paid archive is included here. This is the seller's sample and paid offer, not independent endorsement or verified demand.

Released under the MIT licence (see LICENSE). The licence covers this sample only, not the paid kit.

## Lor
542 LORs, CSV von FIS, GeoJSON von OpenData, rewound

## Children
542 Kinder/Lor, XLSX von Statistikamt berlin brandenburg, erste Hälfte 2021
542 kinderarmut prozent/lor, gescraped von FIS, 2020 12
611899 children in total
299145 children between 6-15
223907 children <6

## childpoverty
542 disctricts
6 invalid (below 300 inhabitants)
december 2020

## Playgrounds
1873 playgrounds
    CSV von FIS, 
    GeoJSON von WFS, 
    rewound und EPSG:25833 to EPSG:4326, 
    one duplicate deleted
        id: 00008100:002d9762
        objektnummer: 40232
        ort: jenneweg, spandau
    decimal error with playground
        id: 00008100:0011df68
        plr_id: 05100209
        ort: falkenhagener weg

1797 accreditable as playground
data from 01.03.2023

2263312.09 sqm playground in total
1259.4947634947134 sqm mean area
875 sqm median area

## Children x Playground
3.6988327975695334 sqm per child in Berlin
7.5659365525079805 sqm per 6-15 child in Berlin
10.108268566860348 sqm per <6 child in Berlin


340.511407902059 children per usable playground
166.46911519198665 6-15 children per usable playground
124.60044518642181 <6 children per usable playground

Correlation Poverty/Playgroundarea:  -0.07403848106566366
Max area/children: 38.10
Min area/children: 0
First quartile pl_area_per_child is:  1.9022556390977443
Third quartile pl_area_per_child is:  5.486561879540167

## LOR x Playground

72 intersections of playgrounds with more than one LOR
501 LOR with at least one playground in them


# Limitations
## Playgrounds
- some playgrounds do not seem to be in the cities registry
- parks are not included in the analysis and might be better than a playground
- not all playgrounds had effective playarea

## LOR
- borders arbitrary, playgrounds within as well
    - mitigation by calculating adjunctness

## children
- poverty data from 2020/12, population from 2021/6
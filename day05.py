def load_data(fp):
    seeds = None
    mappings = []
    
    with open(fp) as f:
        seeds = list(map(int, f.readline()[6:].split()))
        f.readline()
        current_mapping = None
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue

            if line.endswith('map:'):
                current_mapping = []
                mappings.append(current_mapping)
                continue
            
            current_mapping.append(tuple(map(int, line.split())))
    
    return seeds, mappings



def p1(fp):
    seeds, mappings = load_data(fp)
    locations = []
    for seed in seeds:
        x = seed
        for mapping in mappings:
            for dst_start, src_start, length in mapping:
                if x>=src_start and x<src_start+length:
                    offset = x - src_start
                    x = dst_start + offset
                    break
        locations.append(x)
    
    print(min(locations))


def p2(fp):
    seeds, mappings = load_data(fp)
    processing = []
    for i in range(len(seeds)//2):
        start = seeds[2*i]
        length = seeds[2*i + 1]
        end = start + length - 1
        processing.append((start, end))

    mapped_intervals = []
    for mapping in mappings:
        for start, end in processing:
            mapped_intervals.extend(range_map(start, end, mapping))

        
        processing.clear()
        processing, mapped_intervals = mapped_intervals, processing
    
    location_min, _ = min(processing, key=lambda v:v[0])
    print(location_min)
        

        
    




def range_map(start, end, mapping) -> list:
    # obavlja preslikavanje interval [start, end] -> lista intervala
    # NPR. za seed-to-soil
    # range_map(95, 101, ...)
    # ispadne lista [(50, 51), (97, 99), (100, 101)]
    # poredak nebitan
    
    processing = [(start, end)]
    remaining = []
    mapped_intervals = []
    
    for dst_start, src_start, length in mapping:
        src_end = src_start + length - 1
        dst_end = dst_start + length - 1 # inclusive

        for l,r in processing:
            if l>=src_start and l<=src_end and r>=src_start and r<=src_end:
                # interval [l,r] u potpunosti unutar [src_start, src_end]
                # dakle cijeli se odjednom preslikava
                offset_left = l - src_start
                offset_right = r - src_start
                mapped_intervals.append(
                    (dst_start + offset_left, dst_start + offset_right)
                )

            elif l<src_start and r>=src_start and r<=src_end:
                # interval [l,r] je "ispao" s lijeve strane ali ne potpuno
                # preslikava se samo presjek koji je unutra, dakle [src_start, r]
                # ostatak [l, src_start-1] ide na daljnju obradu u listu remaining
                remaining.append((l, src_start-1))
                offset_right = r - src_start
                mapped_intervals.append(
                    (dst_start, dst_start+offset_right)
                )

            elif r>src_end and l>=src_start and l<=src_end:
                # "ispao" s desne strane ali ne potpuno
                remaining.append((src_end+1, r))
                offset_left = l - src_start
                mapped_intervals.append(
                    (dst_start + offset_left, dst_end)
                )

            elif r<src_start or l>src_end:
                # disjunktni intervali
                remaining.append((l, r))

            elif r>src_end and l<src_start:
                # interval [src_start,src_end] u potpunosti unutar [l,r]
                # 3 dijela: [l, src_start-1], 
                # [src_start,src_end], 
                # [src_end+1, r]
                remaining.append((l, src_start-1))
                remaining.append((src_end+1, r))
                mapped_intervals.append((dst_start, dst_end))

            else:
                raise Exception('Ne smije se dogoditi')
                

        processing.clear()
        processing, remaining = remaining, processing

    # jedini preostali intervali su oni koji preslikavaju sami u sebe
    mapped_intervals.extend(processing)
    return mapped_intervals


if __name__ == '__main__':
    fp = 'input.txt'
    p1(fp)
    p2(fp)
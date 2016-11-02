import sys, os, json

folder = sys.argv[1]
fileid = sys.argv[2]

# hit ids
f = open('visualgenome/' + folder + '/hit_ids_' + fileid + '.txt', 'r')
all_hit_ids = []
for line in f:
  all_hit_ids.append(line.replace('\n', ''))
f.close()

# input file
f = open('visualgenome/' + folder + '/input_' + fileid + '.json', 'r')
all_inputs = []
for line in f:
  all_inputs.append(line)
f.close()

# output file
f = open('visualgenome/' + folder + '/output_' + fileid + '.json', 'r')
done_hits = []
for line in f:
  output = json.loads(line)
  done_hits.append(output['hit_id'])
f.close()

# output is printed out
for i, hit_id in enumerate(all_hit_ids):
  if hit_id in done_hits:
    continue
  print all_inputs[i].replace('\n', '')

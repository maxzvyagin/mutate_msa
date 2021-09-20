#!/bin/bash

N=4

for i in ~/mutate_msa/mutations/*; do
    (
        # .. do your stuff here
        echo "starting task $i.."
        sleep $(( (RANDOM % 3) + 1))
    ) &

    # allow to execute up to $N jobs in parallel
    if [[ $(jobs -r -p | wc -l) -ge $N ]]; then
        # now there are $N jobs already running, so wait here for any job
        # to be finished so there is a place to start next one.
        wait -n
    fi

done

# no more jobs to be started but wait for pending jobs
# (all need to be finished)
wait

echo "all done"
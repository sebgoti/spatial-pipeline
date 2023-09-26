nextflow.enable.dsl=2

params.input = 3
params.parameter_files_name = "elastix_parameters_2D"
params.input_dir = "${projectDir}/elastix_parameter_files"
params.number_rounds = 6
params.fix = "./data/input_images/fixed.tiff"
params.mov = './data/input_images/r*_DAPI.tiff'

def parameterFiles_list = []

for (i in 0..params.input) {
    parameterFiles_list.add("${params.parameter_files_name}_${i}.txt")
}

def parameterFiles_str = parameterFiles_list.join(",")

workflow {
    elastix_dir_ch = Channel.value(params.input_dir)
    elastix_ch = Channel.of(parameterFiles_str)
    fix_ch = Channel.fromPath(params.fix)
    mov_ch = Channel.fromPath(params.mov)
    // TEST_PRINT(elastix_dir_ch, elastix_ch, fix_ch, mov_ch)
    // input_ch = Channel.of(whole_path)
    // TEST_PRINT(input_ch)
    REGISTER(elastix_dir_ch, elastix_ch, fix_ch, mov_ch)
    elastix_ch.view()
    mov_ch.view()
}

process REGISTER {

    input:
    val indir
    val param_files
    path fix
    each path(mov)

    output:
    stdout
    //path '*.txt'

    script:
    """
    $projectDir/bin/register.py -i ${params.input_dir} -p ${param_files} -f ${fix} -m ${mov}
    """
}

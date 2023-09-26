nextflow.enable.dsl=2

workflow {
    
    // TEST_PRINT(elastix_dir_ch, elastix_ch, fix_ch, mov_ch)
    // input_ch = Channel.of(whole_path)
    // TEST_PRINT(input_ch)
    REGISTER()
}

process REGISTER {
    """
    echo $PWD
    """
}

pow:
    // Put your code here
    movq $0, %RAX
    cmpq $0, %RDI
    jz return_rax

    movq $1, %RAX
    cmpq $0, %RSI
    jz return_rax

    movq %RDI, %RAX

multi_rax:
    cmpq $1, %RSI
    jz return_rax
    mulq %RDI
    subq $1, %RSI
    jmp multi_rax

return_rax:
    ret
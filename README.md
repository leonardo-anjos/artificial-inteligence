
## Trabalho II - Inteligência Artificial

Centro Universitário Farias Brito <br>
Ciência da Computação <br>
Antonio Leonardo Anjos dos Santos - 1511710

## uberEats

Esse controlador estima o valor da gorgeta que devemos dar a um entregador usando um serviço delivery, e possui determinada estrutura:


**Entrada**

1) Qualidade da comida
    - Conjunto universo: Quão saborosa era a comida, numa escala de 1 a 10?
    - Conjunto difuso: ruim, boa, ótima

2) Serviço de entrega
    - Conjunto universo: O que achou do valor que foi cobrado sobre o serviço prestado pela uberEats, 
      em uma escala  de 1 a 10?
    - Conjunto difuso: baixo custo, aceitável, caro

**Saída**

1) Gorjeta
    - Conjunto universo: quanto devemos dar gorjeta ao motoboy, numa escala de 0% a 25% do valor total?
    - Conjunto difuso: baixo, médio, alto
    
2) Regras
    - Se o serviço de entrega foi bom ou a qualidade da comida era boa, então a gorgeta será alta
    -              ||             médio, então a gorgeta será média
    -              ||             ruim e a qualidade dos alimentos foi ruim, então a gorgeta será baixa

3) Uso
    - Se eu disser a este controlador que eu avaliei:
        o serviço como ***9.8***, e a qualidade como ***6.5***
    
    - Recomendaria que eu daria:
        uma gorgeta de ***20,2%*** baseado no valor total

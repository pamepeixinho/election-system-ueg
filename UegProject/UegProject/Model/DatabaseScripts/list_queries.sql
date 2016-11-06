SELECT EL.Nome, CAR.Cargo, E.Estado
                           FROM tb_candidato AS CA
                           INNER JOIN tb_eleitor AS EL ON CA.CPF = EL.CPF
                           LEFT JOIN tb_estado AS E ON CA.Estado_id = E.Estado_id 
                           INNER JOIN tb_cargo AS CAR ON CA.Cargo_id = CAR.cargo_id;
import GOES

GOES.download('goes16', 'GLM-L2-LCFA', 
              DateTimeIni='20240425-000000', 
              DateTimeFin='20240512-235959',
              path_out='Downloads/')
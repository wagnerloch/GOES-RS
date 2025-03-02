import GOES

GOES.download('goes16', 'GLM-L2-LCFA', 
              DateTimeIni='20240501-000000', 
              DateTimeFin='20240503-235959',
              path_out='Downloads/',
              rename_fmt='%Y%m%d%H%M%S')
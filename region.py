# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Imports
import pandas as pd
import numpy as np
 

# Functions


# Modules


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Constants
MESSAGE = "Hello World !"
PATH_DEPARTEMENTS = "./data/departements-france.csv"
PATH_ZONE_REGIONS = './data/zone-scolaire.csv'

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Functions
class DepartmentInfo:
    
#------------------------------------------------------------------------------
    try:
        data = pd.read_csv(PATH_DEPARTEMENTS, sep=",")
    except FileNotFoundError as e:
        raise Exception(f"File not found at {PATH_DEPARTEMENTS}. DepartmentInfo class cannot be initialized.\nOrigin : {e}")
    except pd.errors.EmptyDataError as e:
        raise Exception(f"The file at {PATH_DEPARTEMENTS} is empty. DepartmentInfo class cannot be initialized.\nOrigin : {e}")
    
    try:
        zone_regions = pd.read_csv(PATH_ZONE_REGIONS, sep=",")
    except FileNotFoundError as e:
        raise Exception(f"File not found at {PATH_ZONE_REGIONS}. DepartmentInfo class cannot be initialized.\nOrigin : {e}")
    except pd.errors.EmptyDataError as e:
        raise Exception(f"The file at {PATH_ZONE_REGIONS} is empty. DepartmentInfo class cannot be initialized.\nOrigin : {e}")
      
    
#------------------------------------------------------------------------------    
    def __init__(self):
        """
        Initializes the DepartmentInfo class with the DataFrame containing department information.

        Parameters:
        data : pd.DataFrame
            The DataFrame containing information about departments.
            It should contain the column 'code_departement' and 'nom_departement'.
        """
       
    def __str__(self):
        """
        Returns a string representation of the DepartmentInfo object.
       
        Returns:
        str
            A string representation containing DataFrame
            and the DataFrame size.
        """
        return f"DataFrame Size: {self.data.shape}\n{str(self.data.head(5))}"

#------------------------------------------------------------------------------
    @staticmethod
    def get_code_department_from_zip(zip_code: str or int) -> str:
        """
        Returns the department code corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the department code is requested.
            Can be either an integer or a string.

        Returns:
        str
            The department code corresponding to the given postal zip code, as a string.
            If no corresponding department code is found, it returns an empty string ("").

        Remarks:
        - Make sure the zip code is in a valid format.
        - The department code is usually the first two digits of the zip code in France.
        - This method supports zip codes as integers or strings.
        """
        if isinstance(zip_code, int):
            zip_code = str(zip_code)
        if not zip_code.isdigit() or len(zip_code) != 5:
            return ""
        return zip_code[:2]

    @classmethod
    def get_region_code_from_postal_zip(cls, zip_code: str or int) -> str or None:
        """
        Returns the region code corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the region code is requested.
            Can be either an integer or a string.

        Returns:
        str or None
            The region code corresponding to the given postal zip code, as a string.
            If no corresponding region code is found, it returns None.

        Remarks:
        - This method internally uses the 'get_code_department_from_zip' method.
        """
        code_department = cls.get_code_department_from_zip(zip_code)
        row = cls.data[cls.data['code_departement'] == str(code_department)]['code_region']
        return row.iloc[0] if not row.empty else None

    @classmethod
    def get_region_name_from_postal_zip(cls, zip_code: str or int) -> str or None:
        """
        Returns the region name corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the region name is requested.
            Can be either an integer or a string.

        Returns:
        str or None
            The region name corresponding to the given postal zip code, as a string.
            If no corresponding region is found, it returns None.

        Remarks:
        - This method internally uses the 'get_code_department_from_zip' method.
        """
        code_department = cls.get_code_department_from_zip(zip_code)
        row = cls.data[cls.data['code_departement'] == str(code_department)]['nom_region']
        return row.iloc[0] if not row.empty else None

    @classmethod
    def get_department_name_from_zip(cls, zip_code: str or int) -> str or None:
        """
        Returns the department name corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the department name is requested.
            Can be either an integer or a string.

        Returns:
        str or None
            The department name corresponding to the given postal zip code, as a string.
            If no corresponding department is found, it returns None.

        Remarks:
        - This method internally uses the 'get_code_department_from_zip' method.
        """
        code_department = cls.get_code_department_from_zip(zip_code)
        row = cls.data[cls.data['code_departement'] == str(code_department)]['nom_departement']
        return row.iloc[0] if not row.empty else None
    
    @classmethod
    def get_zone_from_zip(cls, zip_code: str or int) -> str or None:
        """
        Returns the zone (A, B, or C) corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the zone is requested.
            Can be either an integer or a string.

        Returns:
        str or None
            The zone (A, B, or C) corresponding to the given postal zip code.
            If the postal zip code is not found or the zone is not allocated, it returns None.
        """
        department_code = cls.get_code_department_from_zip(zip_code)
        if department_code is not None:
            row = cls.zone_regions[cls.zone_regions["Department_Codes"].str.contains(department_code)]["Zone"]
            if not row.empty:
                return row.iloc[0]
        return None
    
    @classmethod
    def get_academic_region_from_zip(cls, zip_code: str or int) -> str or None:
        """
        Returns the academic region corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the academic region is requested.
            Can be either an integer or a string.

        Returns:
        str or None
            The academic region corresponding to the given postal zip code, as a string.
            If no corresponding academic region is found, it returns None.
        """
        department_code = cls.get_code_department_from_zip(zip_code)
        if department_code is not None:
            row = cls.zone_regions[cls.zone_regions["Department_Codes"].str.contains(department_code)]["Academic_Region"]
            if not row.empty:
                return row.iloc[0]
        return None
    
    @classmethod
    def get_academy_from_zip(cls, zip_code: str or int) -> str or None:
        """
        Returns the academy corresponding to a given postal zip code.

        Parameters:
        zip_code : int or str
            The postal zip code for which the academy is requested.
            Can be either an integer or a string.

        Returns:
        str or None
            The academy corresponding to the given postal zip code, as a string.
            If no corresponding academy is found, it returns None.
        """
        department_code = cls.get_code_department_from_zip(zip_code)
        if department_code is not None:
            row = cls.zone_regions[cls.zone_regions["Department_Codes"].str.contains(department_code)]["Academies"]
            if not row.empty:
                return row.iloc[0]
        return None



#------------------------------------------------------------------------------
    

   

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
if __name__=="__main__":
    department_info = DepartmentInfo()

    zip_code = "80000"
    department_name = department_info.get_region_name_from_postal_zip(zip_code)

    
    zone = department_info.get_zone_from_zip(zip_code)
    print(f"Zone for postal zip code {zip_code}: {zone}")
    
    academic_region = department_info.get_academic_region_from_zip(zip_code)
    print(f"Academic Region for postal zip code {zip_code}: {academic_region}")

    academy = department_info.get_academy_from_zip(zip_code)
    print(f"Academy for postal zip code {zip_code}: {academy}")





        


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
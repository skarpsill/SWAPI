---
title: "SldWorks::GetMassProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetMassProperties.htm"
---

# SldWorks::GetMassProperties

This method is obsolete and has been superseded
by[SldWorks::GetMassProperties2](sldworksAPI.chm::/SldWorks/SldWorks__GetMassProperties2.htm).

Description

This method gets the mass properties from the
given document for a given configuration

Syntax (OLE Automation)

retval = SldWorks.GetMassProperties (filePathName, configurationName)

(Table)=========================================================

| Input: | (BSTR) filePathName | Name of the document to use formatted as the
filename and extension; is not the fully qualified path name returned
by ModelDoc2::GetPathName and Component2:GetPathName |
| --- | --- | --- |
| Input: | (BSTR) configurationName | Configuration to use |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles containing
the mass property information |

Syntax (COM)

status = SldWorks->IGetMassProperties ( BSTR filePathName,
BSTR configurationName, double* mPropsData, VARIANT_BOOL* retval )

(Table)=========================================================

| Input: | (BSTR) filePathName | Name of the document to use formatted as the
bare filename and extension; is not the fully qualified path name returned
by ModelDoc2::GetPathName and Component2:GetPathName |
| --- | --- | --- |
| Input: | (BSTR) configurationName | Configuration to use |
| Output: | (double*) retval | Array of doubles containing the mass property
information |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is a 0-based array of doubles
as follows:

[CenterOfMassX, CenterOfMassY,
CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX,
MomYZ]

The density of the SolidWorks part is not explicitly
available. However, this value can be backed out using the Volume and
Mass values and the following calculation:

Density = (Mass/Volume)

Consistent with all other API functions, metric
units are returned unless otherwise specified.

It is not necessary for the document to be open
to get the mass properties if the following application-level setting
is enabled:

SldWorks::SetUserPreferenceToggle swUpdateMassPropsDuringSave

In this case, SolidWorks retrieves the mass property
information directly from the file without having to load any of its components.
If this setting is disabled, this information is not present and SolidWorks
returns NULL values.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SldWorks\SldWorks__GetMassProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

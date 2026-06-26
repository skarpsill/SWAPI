---
title: "SldWorks::DateCode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__DateCode.htm"
---

# SldWorks::DateCode

This
method is obsolete and has been superseded by[SldWorks::RevisionNumber](sldworksAPI.chm::/SldWorks/SldWorks__RevisionNumber.htm).

Description

This method returns the date code of the SolidWorks executable. The
date code may also be referred to as the SolidWorks version or revision
number for executables.

Syntax (OLE Automation)

retval = SldWorks.DateCode ()

(Table)=========================================================

| Return: | (long) retval | 7-digit date code of the SolidWorks executable |
| --- | --- | --- |

Syntax (COM)

status = SldWorks->DateCode ( &retval
)

(Table)=========================================================

| Output: | (long) retval | 7-digit date code of the SolidWorks executable |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can also fined the date code by interactively clickingHelp,
Aboutfrom your SolidWorks session. A sample value returned from
this method might be 1998202.

Incremental software releases are provided in between the major releases.
Because new APIs are often added to these incremental releases, this method
is useful for determining whether an API exists in the running release.

For example, if a new API called SldWorks::AddOrdinateDimension was
added to the second incremental release of SolidWorks 98Plus, then the
date code for this incremental release was 1998341. To avoid runtime problems
at customer sites, check the version release number that your customer
is running.

long runningVersion = 0;

hres = myApp->getSWApp()->DateCode(
&runningVersion);

if (runningVersion >= 1998341)

retval = m_DrawDoc->AddOrdinateDimension
(swHorizontalOrdinate, LocX, LocY, LocZ );

The following list shows the date codes for the major releases of SolidWorks.
This list does not include alpha, beta, or pre-releases versions, and
it does not include any version numbers for the incremental releases that
occur in between the major releases.

- SolidWorks 95 95359
- SolidWorks
  96 96175
- SolidWorks 97 97001
- SolidWorks 97Plus 97215
- SolidWorks 98 1998083
- SolidWorks 98Plus 1998293
- SolidWorks 99 1999207
- SolidWorks
  2000
- Use
  SldWorks::RevisionNumberfor
  all versions of SolidWorks later than SolidWorks 2000

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZGetVersion$$**$$ZYear2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\SldWorks\SldWorks__DateCode.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

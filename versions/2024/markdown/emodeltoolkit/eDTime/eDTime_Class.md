---
title: "eDTime Class"
project: ""
interface: "eDTime"
member: ""
kind: "class"
source: "emodeltoolkit/eDTime/eDTime_Class.htm"
---

# eDTime Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DocumentStructureClasses$$**$$eDSerializerParams$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\eModelToolkit\eDTime\eDTime_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

Contains the date and time that the file will expire or not open.

#### Header file code

class ED_API eDTime

{

static eDTime GetCurrentTime();

eDTime();

eDTime( time_t time );

//nMonth : 1=Jan

eDTime( int nYear, int nMonth, int nDay,
int nHour, int nMin, int nSec,int nDST = -1 );

bool IsValid() const;

time_t GetTime() const;

};

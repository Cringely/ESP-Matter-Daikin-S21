import sys
import pcbnew
import wx
_app = wx.App(False)
wx.DisableAsserts()
try:
    wx.Log.EnableLogging(False)
except Exception:
    pass
b = pcbnew.LoadBoard(sys.argv[1])
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
pcbnew.SaveBoard(sys.argv[1], b)

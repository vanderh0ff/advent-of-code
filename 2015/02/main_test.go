package main

import (
	"testing"
)

func TestGetTotalWrappingPapperNeeded(t *testing.T) {
	res1 := getTotalWrappingPapperNeeded(2,3,4)
	if  res1 != 58 {
		t.Log("2x3x4 did not equal 58 it was ", res1)
		t.Fail()
	}
	res2 := getTotalWrappingPapperNeeded(1,1,10)
	if  res2 != 43 {
		t.Log("1x1x10 did not equal 43 it was ", res2)
		t.Fail()
	}
}
func TestGetTotalRibbonNeeded(t *testing.T) {
	res1 := getTotalRibbonNeeded(2,3,4)
	res2 := getTotalRibbonNeeded(1,1,10)
	if res1 != 34 {
		t.Log("2 3 4 is not 34 was ", res1)
		t.Fail()
	}
	if res2 != 14 {
		t.Log("1 1 10 is not 14 was ", res2)
		t.Fail()
	}
}

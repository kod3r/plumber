package shell_test

import (
	"github.com/qadium/plumber/shell"
	"io/ioutil"
	"log"
	"syscall"
	"testing"
	"time"
)

func TestRunAndLog(t *testing.T) {
	err := shell.RunAndLog("true")
	if err != nil {
		t.Error(err)
	}
}

func TestRunAndLogFails(t *testing.T) {
	err := shell.RunAndLog("-notlikely-to-be-a*-cmd")
	if err == nil {
		t.Error("Expected an error but never got one!")
	}
}

func TestInterrupt(t *testing.T) {
	// set the interrupt handler to go off after 50 milliseconds
	go func() {
		time.Sleep(50 * time.Millisecond)
		syscall.Kill(syscall.Getpid(), syscall.SIGINT)
	}()

	err := shell.RunAndLog("/bin/bash", "-c", "while true; do true; done")
	if err == nil || err.Error() != "signal: interrupt" {
		t.Error("Should've received a SIGINT")
	}
}

func BenchmarkRunAndLog(b *testing.B) {
	log.SetOutput(ioutil.Discard)
	for i := 0; i < b.N; i++ {
		shell.RunAndLog("echo", "true")
	}
}
